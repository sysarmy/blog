---
Title: "Cómo gestionar múltiples servidores sin volverse loco"
Description: "ssh config, ProxyJump, multiplexación, tmux, claves y clientes gráficos: cómo ordenar el caos cuando gestionas decenas de servidores."
Keywords:
- ssh
- openssh
- bastion
- proxyjump
- tmux
- sysadmin
Tags:
- sysarmy
- ssh
- herramientas
- sistemas
- seguridad
Thumbnail: assets/gestionar-multiples-servidores.png
socialImage: assets/gestionar-multiples-servidores.png
featuredImage: assets/gestionar-multiples-servidores.png
Topics:
- ssh
- herramientas
- sistemas
markup: markdown
date: 2026-10-22
draft: false
---

Todo empieza con un par de servidores y un `ssh usuario@ip`. Luego llegan staging, los clientes, las VPN, el bastión para llegar a producción, el switch por consola serie y el Windows Server que alguien sigue necesitando por RDP. Y un día tienes quince pestañas abiertas, un `.txt` con contraseñas que no debería existir y la duda de siempre: *¿esta terminal es la de staging o la de producción?*

Vamos a ordenar ese caos por capas: primero lo que ya trae OpenSSH (que es muchísimo), después tmux y, al final, un repaso a los clientes gráficos.

<!--more-->

## 1. Un `~/.ssh/config` que trabaje por ti

Deja de escribir `ssh -i ~/.ssh/cliente_a -p 2222 deploy@10.20.30.40`. Ponle nombre:

```ssh-config
Include config.d/*

Host prod-*
    User admin
    IdentityFile ~/.ssh/prod_ed25519

Host prod-db
    HostName 10.0.1.10

Host *
    IdentitiesOnly yes
    ServerAliveInterval 30
    AddKeysToAgent yes
```

Y ya está: `ssh prod-db`. Ese mismo fichero lo leen `scp`, `rsync`, `git`, Ansible y Remote-SSH de VS Code. En Windows está en `C:\Users\<usuario>\.ssh\config` y funciona igual.

Tres detalles que ahorran sustos:

- **Para cada opción gana el primer valor que encuentra `ssh`**: lo específico va arriba y `Host *` al final.
- **`Include` va arriba del todo** y te permite tener un fichero por cliente en `~/.ssh/config.d/`.
- **`IdentitiesOnly yes`** acaba con el *"Too many authentication failures"* cuando tienes varias claves cargadas.

## 2. Bastiones con `ProxyJump`

Hacer `ssh bastion` y desde ahí otro `ssh` obliga a dejar tu clave en el bastión o a reenviar el agente. Desde OpenSSH 7.3 hay una forma mejor:

```ssh-config
Host prod-*
    ProxyJump bastion
```

El bastión solo hace de túnel: la sesión SSH va cifrada de tu equipo al destino y tu clave no sale de tu máquina. Además, `scp` y `rsync` cruzan el bastión sin hacer nada más. Puedes encadenar saltos (`ProxyJump dmz,interno`), y el nombre del destino lo resuelve el bastión, así que vale el DNS interno.

## 3. Multiplexación: autenticarte una vez

```ssh-config
Host *
    ControlMaster auto
    ControlPath ~/.ssh/sockets/%C
    ControlPersist 10m
```

(Crea antes la carpeta con `mkdir -p ~/.ssh/sockets`.) La primera conexión se queda abierta y las siguientes viajan dentro de ella sin volver a autenticarse. Es oro con segundo factor, con bastiones lentos y con scripts en bucle. `ssh -O exit prod-db` la cierra si se queda colgada al cambiar de red.

Antes de activarlo, ten en cuenta que si se cae la conexión maestra se caen todas, y que quien pueda usar el socket entra sin autenticarse. **No funciona con el OpenSSH nativo de Windows**; desde WSL, sí.

## 4. tmux: que un corte no te mate la migración

Si se cae la VPN a mitad de un `apt upgrade`, adiós. Con tmux la sesión vive en el servidor:

```bash
ssh -t prod-db tmux new -A -s main
```

Te enganchas a la sesión `main` o la creas si no existe. Con `Ctrl-b d` te sales sin cerrarla y, al volver, todo sigue donde lo dejaste. Bonus peligroso: `setw synchronize-panes on` escribe en todos los paneles a la vez; muy útil hasta que te olvidas de desactivarlo antes de un `rm`.

Para tareas largas que no vas a mirar, lo correcto es systemd o cron, no tmux.

## 5. Claves y agentes

- **Una clave Ed25519 por cliente o entorno**, con passphrase y un comentario (`-C`) que diga de quién es. Revocar un acceso no debería afectar a los demás.
- **`ssh-add -t 8h`** carga la clave en el agente con caducidad. En Windows, el servicio `ssh-agent` viene desactivado: actívalo una vez.
- **Nunca `ForwardAgent yes` en `Host *`.** Mientras estás conectado, root en ese servidor puede usar tu agente para entrar como tú en otras máquinas. Para los bastiones ya tienes `ProxyJump`.
- **Claves de servicio limitadas** en `authorized_keys`: `from="10.0.0.0/8",restrict ssh-ed25519 AAAA... backup@nas`.
- **Contraseñas en un gestor** (1Password, Bitwarden, KeePassXC…), nunca en un `.txt`.

## 6. Clientes gráficos: cuando prefieres una ventana para todo

Compensan si trabajas en Windows, mezclas SSH con RDP, VNC o serie, o simplemente no quieres mantener todo a mano.

| Herramienta | Sistemas | Licencia | Lo mejor | Ojo con |
|---|---|---|---|---|
| **PuTTY** | Windows (y Unix) | Libre | Ligero y portable | Muy austero, sin pestañas |
| **MobaXterm** | Windows | Home gratis / Pro de pago | Todo en uno, con X11, SFTP y RDP | La Home limita sesiones y túneles |
| **SecureCRT** | Win, macOS, Linux | De pago | Scripting y redes a gran escala | El SFTP gráfico va aparte |
| **Termius** | Escritorio y móvil | Freemium | Los mismos hosts en todos tus dispositivos | Sincronizar es de pago y pasa por su nube |
| **Tabby** | Win, macOS, Linux | Libre (MIT) | Configurable, con plugins | Electron: consume más |
| **Royal TS/TSX** | Windows / macOS | Gratis hasta 10 conexiones | Pensado para equipos | Sin Linux |
| **Remmina** | Linux | Libre (GPL) | RDP y VNC en Linux | SSH básico |

### Y la mía: SynapTerm

> **Disclaimer:** SynapTerm la he desarrollado yo.

Nació para resolver un problema concreto: los **bastiones de menú**, en los que eliges el destino escribiendo y `ProxyJump` no sirve. SynapTerm encadena esos saltos y **transfiere archivos a través de la propia terminal**. Además:

- SFTP por la misma conexión que la terminal y un **modo IDE** (editor ligero o abrir en VS Code con un clic).
- Envío del mismo comando a varios paneles a la vez.
- Contraseñas en el llavero del sistema y gestión del agente SSH.
- SSH, SFTP, Telnet, serie, RDP y VNC.
- **IA con tu propio agente** (Claude Code, Gemini CLI, Codex) o tu propia clave de API. Por defecto solo lee, cada orden se confirma y las contraseñas nunca se envían al modelo.
- Importa `~/.ssh/config`, MobaXterm y SecureCRT.

Lo que tienes que saber: funciona en **Windows y Linux** (macOS no), es **código cerrado** y es un proyecto joven. La versión gratuita guarda hasta 8 servidores, no incluye RDP ni IA y limita las automatizaciones; puedes [descargarla gratis](https://synapterm.com/download?ref=sysarmy), sin cuenta ni registro. El plan Pro está en beta y puedes pedir acceso en [synapterm.com](https://synapterm.com/#beta) o por Discord (KineticK). Agradezco las críticas más que los elogios.

## Para llevarte

- [ ] Alias en `~/.ssh/config`, un fichero por cliente y `Host *` al final.
- [ ] `ProxyJump` para los bastiones.
- [ ] `ControlMaster` para autenticarte una vez.
- [ ] tmux para lo que no puede morir.
- [ ] Una clave por contexto y `ForwardAgent` lejos de `Host *`.
- [ ] Cero contraseñas en `.txt`.

Si tienes tus propios trucos, compártelos con la comunidad: seguro que hay alguno que no conozco.
