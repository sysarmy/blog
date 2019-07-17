---
Description: "Sysarmy - Comunidad de sistemas"
Keywords:
- sysadmin 
- sistemas
- desarrollo
- developer
- administración de sistemas
- administrador de sistemas
- linux
- cloud
- docker
- kubernetes
Section: 
Slug: the-missing-introduction-to-containerization
Tags:
- sysarmy
Thumbnail: /blog/assets/0_D6D2UV47p42ACOnu.jpeg
Title: The missing introduction to containerization
Topics:
- Development
- Leadership
- Systems
Url: 2019/07/11/the-missing-introduction-to-containerization
date: 2019-07-11
draft: true
---

<p>Photo by 
<a href="https://unsplash.com/@fancycraveofficial?utm_source=medium&utm_medium=referral" target="_blank"> Fancy Crave</a> on 
<a href="https://unsplash.com/?utm_source=medium&utm_medium=referral" target="_blank"> Unsplash</a></p>

<p>Original link: <a href="https://medium.com/faun/the-missing-introduction-to-containerization-de1fbb73efc5" target="_blank"> https://medium.com/faun/the-missing-introduction-to-containerization-de1fbb73efc5</a></p>

During the last four years from 2015 to 2019, cloud and distributed computing were one of the most in-demand skills. They graduated from a niche skillset to a more prominent skillset in the global workforce. Containerization technologies are one of the trendiest topics in the cloud economy and the IT ecosystem. The container ecosystem can be confusing at times, this post may help you understand some confusing concepts about Docker and containers. We are also going to see how the containerization ecosystem evolved and the state of containerization in 2019.

<blockquote><p>We are not makers of history. We are made by history.</p>Martin Luther King</blockquote>

Docker is one of the most known containers platforms nowadays and it was released in 2013. However, the use of isolation and containerization started before this date. Let’s go back to the year 1979 when we started using the Chroot Jail and see the most known containerization technologies that came after. This will help us understand new concepts not necessarily related to history but also to technology.

<p>{{< figure src="assets/1_xPtUIKBjv2EmJ7mFur0v8w.png" link="assets/1_xPtUIKBjv2EmJ7mFur0v8w.png" >}}</p>

It all started when the <b>Chroot Jail</b> and the Chroot system call were introduced during the development of Version 7 Unix in 1979. Chroot jail is for “Change Root” and it’s considered as one of the first containerization technologies. It allows you to isolate a process and its children from the rest of the operating system. The only problem with this isolation is that a root process can easily exit the chroot. It was never intended as a security mechanism. The <b>FreeBSD Jail</b> were introduced in FreeBSD OS in the year 2000 and it was intended to bring more security to the simple Chroot file isolation. Unlike the Chroot, FreeBSD implementation isolates also the processes and their activities to a particular view of the filesystem.

<p>{{< figure src="assets/0_djtuZOsRL5p5-nnN.gif" link="assets/0_djtuZOsRL5p5-nnN.gif" >}}</p>
<p>A Chroot Jail. Source: <a href="https://linuxhill.wordpress.com/2014/08/09/014-setting-up-a-chroot-jail-in-crunchbang-11debian-wheezy" target="_blank">https://linuxhill.wordpress.com/2014/08/09/014-setting-up-a-chroot-jail-in-crunchbang-11debian-wheezy</a></p>

When the operating system-level virtualization capabilities were added to the Linux kernel, <b>Linux VServer</b> was introduced in 2001 and it used both a chroot-like mechanism combined with “security contexts” and operating system-level virtualization (containerization) to provide a virtualization solution. It is more advanced than the simple chroot and it lets you run multiple Linux distributions on a single distribution (VPS).

<p>{{< figure src="assets/0_4gCjTj4G7Mamh3Iw.png" link="assets/0_4gCjTj4G7Mamh3Iw.png" >}}</p>

In <b>February 2004</b>, Oracle released <b>Oracle Solaris Containers</b>, an implementation of Linux-Vserver for X86 and SPARC processors.

<p>SPARC is a RISC (reduced instruction set computing) architecture developed by Sun Microsystems. </p>
A Solaris Container is a combination of system resource controls and the boundary separation provided by “zone”.

<p>{{< figure src="assets/0_hB4RZW-bDUp8Y5vn.png" link="assets/0_hB4RZW-bDUp8Y5vn.png" >}}</p>
<p>Oracle Solaris 11.3</p>

Similar to Solaris Containers, the first version of <b>OpenVZ</b> was introduced in 2005. OpenVZ, like Linux-VServer, uses the OS-level virtualization and it was adopted by many hosting companies to isolate and sell VPSs. OS-level virtualization has some limits since containers share the same architecture and kernel version the disadvantage happens in situations where guests require different kernel versions than that of the host.

Linux-VServer and OpenVZ require patching the kernel to add some control mechanisms used to create an isolated container. OpenVZ patches were not integrated into the Kernel.

<p>{{< figure src="assets/0_uOQ2Hw4g57cCffs_.png" link="assets/0_uOQ2Hw4g57cCffs_.png" >}}</p>

In 2007, Google released <b>CGroups</b>, a mechanism that limits and isolates the resource usage (CPU, memory, disk I/O, network, etc.) of a collection of processes. CGroups was, as opposed to OpenVZ Kernel, mainlined into the Linux kernel in 2007.

In 2008, the first version of <b>LXC</b> (Linux Containers) was released. LXC is similar to OpenVZ, Solaris Containers and Linux-VServer, however, it uses CGroups which is already implemented in the Linux Kernel. Then CloudFoundry created <b>Warden</b> in 2013, an API to manages isolated, ephemeral, and resource controlled environments. In its first versions, Warden used LXC.

<p>{{< figure src="assets/0_3ecAWOU0bx8b8ZJg.png" link="assets/0_3ecAWOU0bx8b8ZJg.png" >}}</p>

In 2013, the first version of <b>Docker</b> was introduced. It performs, like OpenVZ and Solaris Containers, operating-system-level virtualization.

In 2014, Google introduced <b>LMCTFY</b> ( Let me contain that for you), the open source version of Google’s container stack, which provides Linux application containers. Google engineers have been collaborating with Docker over libcontainer and porting the core concepts and abstractions to libcontainer. So the project is not actively being developed and in the future, the core of this project will be probably replaced by libcontainer.

LMCTFY run applications in isolated environments on the same Kernel and without patching it since it uses CGroups, Namespaces and other Linux Kernel features.

<p>{{< figure src="assets/0_LM_h7DBEtWP7u3-D.jpeg" link="assets/0_LM_h7DBEtWP7u3-D.jpeg" >}}</p>
<p>Photo by <a href="https://unsplash.com/@pawel_czerwinski?utm_source=medium&utm_medium=referral" target="_blank"> Paweł Czerwiński</a> on <a href="https://unsplash.com/?utm_source=medium&utm_medium=referral" target="_blank"> Unsplash</a></p>

Google is a leader in the container industry. Everything at Google runs on containers. There are <a href="https://speakerdeck.com/jbeda/containers-at-scale" target="_blank">more than 2 billion containers</a> running on Google infrastructure every week.

In December 2014, CoreOS released and started to support rkt (initially released as Rocket) as an alternative to Docker.

<p>{{< figure src="assets/0_tPm8po0uPkzCncip.jpg" link="assets/0_tPm8po0uPkzCncip.jpg" >}}</p>

<h2>Jails, Virtual Private Servers, Zones, Containers, and VMs</h2>

Isolation and resource control are the common goals behind using <b>Jails</b>, <b>Zones</b>, <b>VPSs</b>, <b>VMs</b>, and <b>Containers</b> but every technology use different ways to achieve it, has its limits and its advantages.

Until now, we have briefly seen how a Jail work and we introduced how Linux-VServer allows running isolated user spaces in which computer programs run directly on the host operating system’s kernel but have access to a restricted subset of its resources.

Linux-VServer allows running <b>“Virtual Private Servers”</b> and host kernel must be patched to use it. (Consider VPS as the commercial name.)

Solaris containers are called Zones.

A <b>“Virtual Machine”</b> is a generic term to describe an emulated virtual machine on top of a “real hardware machine”. The term was originally defined by Popek and Goldberg as an efficient, isolated duplicate of a real computer machine.

Virtual machines can be either <b>“System Virtual Machines”</b> or <b>“Process Virtual Machines”</b>. In our everyday use of the word VMs, we usually mean “system virtual machines” which is the emulation of the host hardware to emulate an entire operating system. However, “Process Virtual Machine”, sometimes called “Application Virtual Machine”, are used to emulate the programming environment for the execution of an individual process: Java Virtual Machine is an example.

The <b>OS Level virtualization</b> is also called <b>containerization</b>. Technologies like Linux-VServer and OpenVZ can run multiple operating systems while sharing the same architecture and kernel version.

Sharing the same architecture and kernel have some limitations and disadvantages in situations where guests require different kernel versions than that of the host.

<p>{{< figure src="assets/0_ReM7IT-89RvS5d6X.png" link="assets/0_ReM7IT-89RvS5d6X.png" >}}</p>
<p>Source: <a href="https://fntlnz.wtf/post/why-containers" target="_blank"> https://fntlnz.wtf/post/why-containers</a></p>

System containers (e.g LXC) offer an environment as close as possible as the one you’d get from a VM but without the overhead that comes with running a separate kernel and simulating all the hardware.

<p>{{< figure src="assets/0_LWMO76kzxqar8ZCz.png" link="assets/0_LWMO76kzxqar8ZCz.png" >}}</p>
<p>VM vs Container. Source: Docker Blog</p>

<h1>OS Containers vs App Containers</h1>

OS-level virtualization helps us in creating containers. Technologies like LXC and Docker use this type of isolation. We have two types of containers here:

<li>OS Containers where the operating system with the whole application stack is packaged (example LEMP).</li>
<li>Applications Containers that usually run a single process per container.</li>

In the case App Containers, we would have 3 containers to create a LEMP stack:

<li>PHP server (or PHP FPM).</li>
<li>Web server (Nginx).</li>
<li>Mysql.</li>

<p>{{< figure src="assets/1_wdWFToSOgxLNN8jOP4mMbA.png" link="assets/1_wdWFToSOgxLNN8jOP4mMbA.png" >}}</p>
<p>OS vs App Containers</p>

<h1>Docker: Container or Platform?</h1>
<b>Short answer:</b> Both.

<p>{{< figure src="assets/0_SrqYa7ZxjSJrbxN2.png" link="assets/0_SrqYa7ZxjSJrbxN2.png" >}}</p>

<b>Long answer:</b>

When Docker started it used LXC as a container runtime, the idea was to create an API to manage the container runtime, isolate single processes running applications and supervise the container life cycle and the resources it uses.

In early 2013, the Docker project was to build a “standard container” as we can see in this <a href="https://github.com/moby/moby/commit/0db56e6c519b19ec16c6fbd12e3cee7dfa6018c5" target="_blank">manifesto</a>.

<p>{{< figure src="assets/1_u0-Ax-jljui1RjuwGGNHDQ.png" link="assets/1_u0-Ax-jljui1RjuwGGNHDQ.png" >}}</p>
<p>The standard container manifesto  <a href="https://github.com/docker/docker/commit/eed00a4afd1e8e8e35f8ca640c94d9c9e9babaf7" target="_blank">was removed.</a></p>

<p>{{< figure src="assets/1_nMpyG69J0HdLQ_emYGpwIA.png" link="assets/1_nMpyG69J0HdLQ_emYGpwIA.png" >}}</p>

Docker started building a monolithic application with multiple features from launching Cloud servers to building and running images/containers.

Docker used <b>“libcontainer”</b> to interface with Linux kernel facilities like <b>Control Groups</b> and <b>Namespaces</b>.

<p>{{< figure src="assets/1_vHuyH5qKRJG7CgjRgZ6BjQ.jpeg" link="assets/1_vHuyH5qKRJG7CgjRgZ6BjQ.jpeg" >}}</p>
<p>Docker, Libcontainer and Linux Kernel Facilities</p>

<h2>Let’s Create a Container Using Namespaces & Cgroups</h2>
I am using Ubuntu in this example, but it should be the same for most distros. Start by installing CGroup Tools and stress utility as we are going to make some stress tests.

<pre><p>sudo apt install cgroup-tools</p>
<p>sudo apt install stress</p></pre>

This command will create a new execution context:

<pre><p>sudo unshare --fork --pid --mount-proc bash</p></pre>

<p>{{< figure src="assets/1__0-i8uedAguHFOGQzGrQ-g.gif" link="assets/1__0-i8uedAguHFOGQzGrQ-g.gif" >}}</p>

The <u>'unshare'</u> command disassociates parts of the process execution context

<pre><p><b>unshare()</b> allows a process (or thread) to disassociate parts of its execution context that are currently being shared with other processes (or threads).  Part of the execution context, such as the mount namespace, is shared implicitly when a new process is created using <a href="http://man7.org/linux/man-pages/man2/fork.2.html" target="_blank">fork(2)</a> or <a href="http://man7.org/linux/man-pages/man2/vfork.2.html" target="_blank">vfork(2)</a>, while other parts, such as virtual memory, may be shared by explicit request when creating a process or thread using <a href="http://man7.org/linux/man-pages/man2/clone.2.html" target="_blank">clone(2)</a>.</p></pre>

Now, using  <u>'cgcreate'</u> we can create a Control Groups and define two controllers, one on memory and the other on CPU.

<p>{{< figure src="assets/1_uI9sfocuS3sQ6PtaSyi8sA.gif" link="assets/1_uI9sfocuS3sQ6PtaSyi8sA.gif" >}}</p>

The next step is defining a limit for the memory and activate it:

<pre><p>echo 3000000 > /sys/fs/cgroup/memory/mygroup/memory.kmem.limit_in_bytes</p><p>
cgexec -g memory:mygroup bash</p></pre>

<p>{{< figure src="assets/1_lbKLdVyQANO_g1hngTtqnw.gif" link="assets/1_lbKLdVyQANO_g1hngTtqnw.gif" >}}</p>

Now let’s stress the isolated namespace we created with memory limits.

<pre><p>stress --vm 1 --vm-bytes 1G --timeout 10s</p></pre>

<p>{{< figure src="assets/1_alPkm2pfgcBSlEqFCLUqOQ.gif" link="assets/1_alPkm2pfgcBSlEqFCLUqOQ.gif" >}}</p>

We can notice that the execution is failed, therefore we know that the memory limit is working fine.

If we do the same thing on the host machine (no imitation on a 16G RAM), the test will never fail, unless you really do not have enough free memory:

<p>{{< figure src="assets/1_kM2CAzOdJBMYNsWZE_m4kw.gif" link="assets/1_kM2CAzOdJBMYNsWZE_m4kw.gif" >}}</p>

Following these steps will help in understanding how Linux facilities like <b>CGroups</b> and other resource control features can create and manage isolated environments in Linux systems.

<b>libcontainer</b> interfaces with these facilities to manage and run Docker containers.

<h2>runC: Leveraging libcontainer Without Using Docker</h2>
In 2015, Docker announced runC: a lightweight, portable container runtime.

<p>{{< figure src="assets/0_FNIlNDZ6sh8ZojXe.png" link="assets/0_FNIlNDZ6sh8ZojXe.png" >}}</p>

runC is basically a little command-line tool to leverage libcontainer directly, without going through the Docker Engine.

The goal of runC is to make standard containers available everywhere.

This project was donated the <b>Open Container Initiative (OCI)</b>.

The libcontainer repository has been archived now.

<p>{{< figure src="assets/1_DLWCBYfxl4S0gMTcU_S62w.png" link="assets/1_DLWCBYfxl4S0gMTcU_S62w.png" >}}</p>

In reality, libcontainer was not abandoned but it was moved to runC repository.

<p>{{< figure src="assets/1_5EUdD1n_0jsRqnY8gO8fxQ.png" link="assets/1_5EUdD1n_0jsRqnY8gO8fxQ.png" >}}</p>

Let’s move to the practical part and create a container using runC.

Start by installing runC runtime:

<p>{{< figure src="assets/1_JK9nvaKWMqjcLzTtSwS5cA.gif" link="assets/1_JK9nvaKWMqjcLzTtSwS5cA.gif" >}}</p>

Let’s create a directory (/mycontainer) where we are going to export the content of the image <a href="https://hub.docker.com/_/busybox" target="_blank">Busybox</a>.

<blockquote><p>Coming in somewhere between 1 and 5 Mb in on-disk size (depending on the variant), BusyBox is a very good ingredient to craft space-efficient distributions.</p>
<p><a href="http://www.busybox.net/" target="_blank">Busybox</a> combines tiny versions of many common UNIX utilities into a single small executable. It provides replacements for most of the utilities you usually find in GNU fileutils, shellutils, etc. The utilities in BusyBox generally have fewer options than their full-featured GNU cousins; however, the options that are included provide the expected functionality and behave very much like their GNU counterparts. BusyBox provides a fairly complete environment for any small or embedded system.</p>
<p>Source: Docker Hub.</p></blockquote>

<p>{{< figure src="assets/1_ajEBPmA4hvoNWP1Zjqvy7w.gif" link="assets/1_ajEBPmA4hvoNWP1Zjqvy7w.gif" >}}</p>

Using runC command we can run the busybox container that use the extracted image and a spec file (config.json).

<p>{{< figure src="assets/1_1LoZax4QrTYhydOdc3_prA.gif" link="assets/1_1LoZax4QrTYhydOdc3_prA.gif" >}}</p>

<u>'runc spec'</u> command initially creates this JSON file:

<pre>
{
 "ociVersion": "1.0.1-dev",
 "process": {
  "terminal": true,
  "user": {
   "uid": 0,
   "gid": 0
  },
  "args": [
   "sh"
  ],
  "env": [
   "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
   "TERM=xterm"
  ],
  "cwd": "/",
  "capabilities": {
   "bounding": [
    "CAP_AUDIT_WRITE",
    "CAP_KILL",
    "CAP_NET_BIND_SERVICE"
   ],
   "effective": [
    "CAP_AUDIT_WRITE",
    "CAP_KILL",
    "CAP_NET_BIND_SERVICE"
   ],
   "inheritable": [
    "CAP_AUDIT_WRITE",
    "CAP_KILL",
    "CAP_NET_BIND_SERVICE"
   ],
   "permitted": [
    "CAP_AUDIT_WRITE",
    "CAP_KILL",
    "CAP_NET_BIND_SERVICE"
   ],
   "ambient": [
    "CAP_AUDIT_WRITE",
    "CAP_KILL",
    "CAP_NET_BIND_SERVICE"
   ]
  },
  "rlimits": [
   {
    "type": "RLIMIT_NOFILE",
    "hard": 1024,
    "soft": 1024
   }
  ],
  "noNewPrivileges": true
 },
 "root": {
  "path": "rootfs",
  "readonly": true
 },
 "hostname": "runc",
 "mounts": [
  {
   "destination": "/proc",
   "type": "proc",
   "source": "proc"
  },
  {
   "destination": "/dev",
   "type": "tmpfs",
   "source": "tmpfs",
   "options": [
    "nosuid",
    "strictatime",
    "mode=755",
    "size=65536k"
   ]
  },
  {
   "destination": "/dev/pts",
   "type": "devpts",
   "source": "devpts",
   "options": [
    "nosuid",
    "noexec",
    "newinstance",
    "ptmxmode=0666",
    "mode=0620",
    "gid=5"
   ]
  },
  {
   "destination": "/dev/shm",
   "type": "tmpfs",
   "source": "shm",
   "options": [
    "nosuid",
    "noexec",
    "nodev",
    "mode=1777",
    "size=65536k"
   ]
  },
  {
   "destination": "/dev/mqueue",
   "type": "mqueue",
   "source": "mqueue",
   "options": [
    "nosuid",
    "noexec",
    "nodev"
   ]
  },
  {
   "destination": "/sys",
   "type": "sysfs",
   "source": "sysfs",
   "options": [
    "nosuid",
    "noexec",
    "nodev",
    "ro"
   ]
  },
  {
   "destination": "/sys/fs/cgroup",
   "type": "cgroup",
   "source": "cgroup",
   "options": [
    "nosuid",
    "noexec",
    "nodev",
    "relatime",
    "ro"
   ]
  }
 ],
 "linux": {
  "resources": {
   "devices": [
    {
     "allow": false,
     "access": "rwm"
    }
   ]
  },
  "namespaces": [
   {
    "type": "pid"
   },
   {
    "type": "network"
   },
   {
    "type": "ipc"
   },
   {
    "type": "uts"
   },
   {
    "type": "mount"
   }
  ],
  "maskedPaths": [
   "/proc/kcore",
   "/proc/latency_stats",
   "/proc/timer_list",
   "/proc/timer_stats",
   "/proc/sched_debug",
   "/sys/firmware",
   "/proc/scsi"
  ],
  "readonlyPaths": [
   "/proc/asound",
   "/proc/bus",
   "/proc/fs",
   "/proc/irq",
   "/proc/sys",
   "/proc/sysrq-trigger"
  ]
 }
}
</pre>

<p>{{< figure src="assets/1_4FUjn8I_BEwfjOBYjFJLLQ.gif" link="assets/1_4FUjn8I_BEwfjOBYjFJLLQ.gif" >}}</p>

An alternative for generating a customized spec config is to use “oci-runtime-tool”, the sub-command “oci-runtime-tool generate” has lots of options that can be used to do many customizations.

For more information see <a href="https://github.com/opencontainers/runtime-tools" target="_blank">runtime-tools</a>.

Using the generated specification JSON file, you can customize the runtime of the container. We can, for example, change the argument for the application to execute.

<p>{{< figure src="assets/1_-ygkHyVZ0z2QZ1_tz4v87A.png" link="assets/1_-ygkHyVZ0z2QZ1_tz4v87A.png" >}}</p>

Let’s view the change between the original config.json file and the new one:

<p>{{< figure src="assets/0_rtFur5mV3gHX0qux.png" link="assets/0_rtFur5mV3gHX0qux.png" >}}</p>

Let’s now run again the container and notice how it sleeps for 10 seconds before exiting.

<h2>Industry-standard Container Runtimes</h2>
Since containers become mainstream, the different actors in the containers ecosystem have been working on standardization.
Standardization is a key to automation and generalization of best practices.

While giving the runC project to the OCI, Docker started using <b>containerd</b> in <b>2016</b>, as a container runtime that interface with the underlying low-level runtime runC.

<p>{{< figure src="assets/1_HcjQouxSf_prU577urMVKg.gif" link="assets/1_HcjQouxSf_prU577urMVKg.gif" >}}</p>

Containerd has full support for starting OCI bundles and managing their lifecycle. Containerd (as well as other runtimes like cri-o) uses runC to run containers but implements also other high-level features like image management and high-level APIs.

<p>{{< figure src="assets/1_BR16fUqgeQnwDWFLB40vgg.png" link="assets/1_BR16fUqgeQnwDWFLB40vgg.png" >}}</p>
<p>containerd integration with Docker & OCI runtimes</p>

<h2>Containerd, Shim and RunC, How Everything Work Together</h2>
runC is built on libcontainer which is the same container library previously powering Docker engine.

Prior to version 1.11, Docker engine was used to manage volumes, networks, containers, images etc..

Now, Docker architecture is broken into four components:

<li>Docker engine,</li>
<li>containerd,</li>
<li>containerd-shim</li>
<li>and runC.</li>
The binaries are respectively called <b>docker</b>, <b>docker-containerd</b>, <b>docker-containerd-shim</b>, and <b>docker-runc</b>.

Let’s enumerate the step to run a container using the new architecture of docker:

<li>Docker engine creates the container (from an image) and passes it to containerd.</li>
<li>Containerd calls containerd-shim</li>
<li>Containerd-shim uses runC to run the container</li>
<li>Containerd-shim allows the runtime (runC in this case) to exit after it starts the container</li>

Using this new architecture we can run “daemon-less containers” and we have two advantages:

<li>runC can exit after starting the container and we don’t have to have the whole runtime processes running.</li>
<li>containerd-shim keeps the file descriptors like stdin, stdout and stderr open even when Docker and/or containerd die.</li>

<p>{{< figure src="assets/1_wVGfj16cENwr5Tt7fKX0-A.png" link="assets/1_wVGfj16cENwr5Tt7fKX0-A.png" >}}</p>

<p><b>“If runC and Containerd are both Runtimes, Why the Heck are We using Both to Run a Single Container ?”</b></p>
This is probably one of the most redundant questions. After understanding why Docker broke its architecture to runC and Containerd, you realize that both are runtimes.

If you were following the story from the beginning you had probably noticed the use of high-level and low-level runtimes. This is the practical difference between both. 
Both can be called runtimes but every runtime has a different purpose and features. In order to keep the containers ecosystem standardized, low-level containers runtime only allows running containers.

The low-level runtime (like runC) should be light, fast and not conflictual with other higher levels of containers management.

When you create a Docker container, it is in reality managed by both runtimes containerd and runC.

You can find many containers runtimes, some of them are OCI standarized and others are not, some are low-level runtimes and other are more than just runtimes and implement a tooling layer to manage the lifecycle of containers and more:

<li>image transfer and storage,</li>
<li>container execution and supervision,</li>
<li>low-level storage,</li>
<li>network attachments,</li>
<li>etc..</li>

<p>{{< figure src="assets/0_myxY037T0IIAFm09.png" link="assets/0_myxY037T0IIAFm09.png" >}}</p>
<p>Source: <a href="https://www.ianlewis.org/en/container-runtimes-part-1-introduction-container-r" target="_blank">https://www.ianlewis.org/en/container-runtimes-part-1-introduction-container-r</a></p>

We can add new runtime using Docker by executing:

<pre>sudo dockerd --add-runtime=< runtime-name >=< runtime-path > </pre>
Example:

<pre><p>sudo apt-get install nvidia-container-runtime</p>
<p>sudo dockerd --add-runtime=nvidia=/usr/bin/nvidia-container-runtime</p></pre>

<h2>Container Runtime Interface</h2>

Kubernetes is one of the most popular orchestration systems. With the evolving number of containers runtime, kubernetes aims to be more extensible and interface with more containers runtimes other than Docker.

Originally, Kubernetes used Docker runtime to run containers and it is still the default runtime.

However, CoreOS wanted to use kubernetes with RKT runtime and offered patches to kubernetes to use this runtime as an alternative to Docker.

Instead of changing kubernetes code base when adding a new container runtime, Kubernetes upstream decided to create CRI or Container Runtime Interface, which is a set of APIs and libraries that allows running different containers runtime in Kubernetes.

Any interaction between kubernetes core and a supported runtime is performed through the CRI API.

<p>{{< figure src="assets/1_Pn0MjucH2QPOos-IYVsV0g.png" link="assets/1_Pn0MjucH2QPOos-IYVsV0g.png" >}}</p>

These are some of the CRI plugins:

<b>CRI-O:</b>

Is the first container runtime created for the kubernetes CRI interface. cri-o is not intended to replace Docker but it can be used instead of Docker runtime in the specefic context of Kubernetes.

<p>{{< figure src="assets/0_5mwyLfYuenO_WRvc.png" link="assets/0_5mwyLfYuenO_WRvc.png" >}}</p>

<b>Containerd CRI :</b>

With cri-containerd, users can run Kubernetes clusters using containerd as the underlying runtime without Docker installed.

<p>{{< figure src="assets/0_cMFdXY9o-eDp5Ee0.png" link="assets/0_cMFdXY9o-eDp5Ee0.png" >}}</p>

<b>gVisor CRI:</b>

gVisor is a project developed by Google which implements around 200 of the Linux system calls in userspace, for additional security compared to Docker containers that run directly on top of the Linux kernel and are isolated with namespaces.

<p>{{< figure src="assets/1_wRuQ83mFIABg5YJuzUGd3A.png" link="assets/1_wRuQ83mFIABg5YJuzUGd3A.png" >}}</p>

Google Cloud App Engine uses gVisor CRI to perform an isolation between customers.

gVisro runtime integrates with Docker and Kubernetes, making it simple to run sandboxed containers.

<b>CRI-O Kata Containers</b>

<p>{{< figure src="assets/0_e2Vvo45RxWkVGsEV.jpeg" link="assets/0_e2Vvo45RxWkVGsEV.jpeg" >}}</p>

Kata Containers is an open source project building lightweight virtual machines that plug into the containers ecosystem. CRI-O Kata Containers allows running Kata Containers on Kubernetes instead of Docker default runtime.

<h2>The Moby Project</h2>
The project of building a single monolithic Docker platform is somehow abandoned and gave birth to Moby project where Docker is composed of many components like RunC.

<p>{{< figure src="assets/0_GQt58yi6jkeOkN5o.png" link="assets/0_GQt58yi6jkeOkN5o.png" >}}</p>
<p>Source: Solomon Hykes Twitter</p>

Moby is a project to organize and modularize the development of Docker.

It is an ecosystem of development and production. Regular users of Docker will notice no change.

<p>{{< figure src="assets/0_AVgVB_uX39FmP4iI.png" link="assets/0_AVgVB_uX39FmP4iI.png" >}}</p>
<p>Source: Solomon Hykes Twitter</p>

Moby helps in developing and running Docker CE and EE (Moby is Docker upstream) as well as creating a development and production environment for other runtimes and platforms.

<h2>The Open Containers Initiative</h2>
As we have seen, Docker donated RunC to the <b>Open Container Initiative (OCI)</b>, but what is this initiative ?

The OCI is a lightweight, open governance structure, launched on <b>2015</b> by Docker, CoreOS and other leaders in the container industry.

the Open Container Initiative (OCI) aims to establish common standards for software containers in order to avoid a potential fragmentation and divisions inside the container ecosystem.

<p>{{< figure src="assets/0_eW0xAc3iAJ-PW7qk.png" link="assets/0_eW0xAc3iAJ-PW7qk.png" >}}</p>

It contains two specifications:

<li><b>runtime-spec</b>: The runtime specification</li>
<li><b>image-spec</b>: The image specification</li>
A container using a different runtime can be used with Docker API. A container created using Docker, should run with any other engine.

<h2>Connect Deeper</h2>
<blockquote>If you like this article, let me know by buying me a coffee <a href="https://www.buymeacoffee.com/eon01" target="_blank">here</a> and I’ll publish similar articles explaining advanced concepts in an easy way. You can also order my online training <a href="https://painlessdocker.com/" target="_blank">Painless Docker</a>.</blockquote>

Make sure to follow me on Medium to receive the future articles and subscribe to one or more of my hand curated newsletters and Slack team chat:

<li><a href="http://devopslinks.com/?utm_source=medium&utm_medium=The-Missing-Introduction-To-Containerization" target="_blank">DevOpsLinks</a>: An Online Community Of Thousands Of IT Experts & DevOps Enthusiast From All Over The World.</li>
<li><a href="http://joinshipped.com/?utm_source=medium&utm_medium=The-Missing-Introduction-To-Containerization" target="_blank">Shipped</a>: An Independent Newsletter Focused On Serverless, Containers, FaaS & Other Interesting Stuff</li>
<li><a href="http://kaptain.xyz/?utm_source=medium&utm_medium=The-Missing-Introduction-To-Containerization" target="_blank">Kaptain</a>: A Kubernetes Community Hub, Hand Curated Newsletter, Team Chat, Training & More</li>

