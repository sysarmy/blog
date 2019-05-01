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
Slug: multiple-vulnerabilities-in-openssl-heres-what-you-need-to-do
Tags:
- sysarmy
Thumbnail: /blog/assets/drown-1.png
Title: Multiple Vulnerabilities in OpenSSL – Here’s What You Need to Do
Topics:
- Development
- Leadership
- Systems
Url: 2016/03/21/multiple-vulnerabilities-in-openssl-heres-what-you-need-to-do
date: 2016-03-21
---

<p><em>Originally written by <a href="https://twitter.com/johannorrman" target="_blank">Johan Norrman</a>, CIO at <a href="http://www.detectify.com" target="_blank">Detectify</a> for <strong><a href="http://www.sysarmy.com" target="_blank">sysarmy</a></strong>.</em></p>
<p>&nbsp;</p>
<p>March could have started better for the OpenSSL team. During the last week, the OpenSSL development team published two high impacts CVEs, <a href="https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-0800" target="_blank">CVE-2016-0800</a> and <a href="https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-0703" target="_blank">CVE-2016-0703</a>.</p>
<p>In this blog post, we explain how the CVEs can compromise your security and what steps you can take to stay safe.</p>
<p>&nbsp;</p>
<p><strong>CVE-2016-0800 (DROWN)</strong></p>
<p>You might already have heard about CVE-2016-0800 by its nickname "DROWN". According to <a href="http://drownattack.com" target="_blank">drownattack.com</a> a server is vulnerable to DROWN if it allows SSLv2 connections or if its private key is used on any other server that allows SSLv2 (see CVE-2016-0703 below).</p>
<p><strong>What can happen:</strong> By gaining access on a DROWN vulnerable server the attacker can gain information such as username, passwords, credit card numbers or any other sensitive information sent via the server.</p>
<p><strong>So what should I do:</strong></p>
<ul>
<li>Make sure that you upgrade OpenSSL to the recommended version.
<ul>
<li>if you are using 1.0.1 upgrade to 1.0.1s</li>
<li>if you are using 1.0.2 upgrade to 1.0.2g</li>
</ul>
</li>
<li>Disable SSLv2 - how this is done varies depending on which software you are using.</li>
</ul>
<p>If you are uncertain if you are vulnerable or not, you can use services such as <a href="http://www.detectify.com" target="_blank">Detectify</a>, that will provide you with a warning if you still are running SSLv2 when you run a scan (see photo below).</p>
<p><a href="assets/detectify1.png" rel="attachment wp-att-430"><img class="alignnone wp-image-430 size-large" src="assets/detectify1.png" alt="" width="720" height="329" /></a></p>
<p>&nbsp;</p>
<p><strong>Learn more about DROWN:</strong></p>
<p>If you want to read more about OpenSSL and DROWN we recommend you to dig into <a href="https://www.openssl.org/blog/blog/2016/03/01/an-openssl-users-guide-to-drown/" target="_blank">this blog post</a> from the OpenSSL team.</p>
<p>&nbsp;</p>
<p><strong>CVE-2016-0703</strong></p>
<p>The second issue, CVE-2016-0703, only affects versions of OpenSSL prior to March 19th, 2015 and is fixed in OpenSSL 0.9.8zf, 1.0.0r, 1.0.1m and 1.0.2a.</p>
<p><strong>What can happen:</strong> It allows a remote attacker to commit an efficient divide-and-conquer key recovery attack. So by eavesdropping on the SSLv2 handshake the attacker can determine the SSLv2 private-key, all and all leading up to a way more efficient version of DROWN.</p>
<p><strong>So what should I do:</strong></p>
<ul>
<li>Make sure that you upgrade to OpenSSL 0.9.8zf, 1.0.0r, 1.0.1m and 1.0.2a, depending on what version you are on now.</li>
<li>Read the security information from your software provider to determine if you need to do anything extra to stay secure.</li>
</ul>
<p>&nbsp;</p>
<p><strong>Comments from Detectify:</strong></p>
<p>"Keeping your infrastructure up to date becomes easier as more and more companies are moving into a DevOps culture. The ones responsible for patching and keeping your production environment up to date are now a part of your development team and no longer just responsible for making sure that the servers are running. However, patching your production servers will always be challenge and keeping them patch should always be a top priority" says Detectify’s CIO Johan Norrman.</p>
<p>&nbsp;</p>
