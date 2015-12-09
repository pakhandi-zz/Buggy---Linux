<h1>Buggy : V.2.3</h1>

A batch-testing sublime plug-in for CodeForces
<br><br>
This application is to assist a competitive-programmer in a CodeForces round. This application downloads all the sample test cases for a problem and runs a user&#39;s solution program on all these test cases so that no time is wasted on manual checking of the solution.

For now the application is for C++ users only.
<br>
<br>
<b>NOTE : </b>Please try the Plug-in once before using it in actual contest to avoid any last minute confusions.<br>
<b>Make Sure you have read the <a href="#installation">Installation</a> and <a href="#usage">Usage</a> very very carefully.</b>
<br>

<h3>Index</h3>
<ol>
<li><a href="#requisites">Requisites</a></li>
<li><a href="#installation">Installation</a></li>
<li><a href="#usage">Usage</a></li>
<li><a href="#techused">Technology Used</a></li>
<li><a href="#testing">Testing</a></li>
<li><a href="http://bugecode.com/post.php?pid=121" target="_blank">FAQ</a></li>
</ol>

<a name="requisites"><h3>Requisites</h3></a>
<ul>
<li>Linux (Tested on Ubuntu-14.04)</li>
<li>Internet Connection (it should be working on terminal)</li>
<li>Sublime Text-3
	<ul>
	<li>To check Sublime is installed correctly
		<ol>
		<li>Open a <b>terminal</b> window.</li>
		<li>Run "subl".</li>
		<li>If Sublime opens up, everything is perfect.</li>
		</ol>
	</li>
	</ul>
</li>
<li>A default browser</li>
<li>Working g++
	<ul>
	<li>To check g++ is working
		<ol>
		<li>Open a <b>terminal</b> window.</li>
		<li>Run "g++".</li>
		<li>If it identifies the command, everything is perfect.</li>
		</ol>
	</li>
	</ul>
</li>
<li><b>NOTE : xdg-open command is used. Make suitable replacements/installations (in zx.sh and start.sh).</b></li>
</ul>

<a name="installation"><h3>Installation</h3></a>
<ol>
<li>Download all the files from <a href="https://github.com/pakhandi/Buggy---Linux/archive/V.2.3.zip">here : V.2.3</a>.</li>
<li>Shift the <b>Buggy---Linux</b> and <b>CF</b> folder to <b>~/.config/sublime-text-3/Packages/User/</b></li>
<li>Make sure proper execution permission is given to <b>ini</b> and shell scripts.</li>
<li>Open sublime. GoTo <b>"Tools -> Build System"</b> and select <b>CF</b></li>
<li>If you see <b>Buggy</b> menu in the menu-bar, installation is complete</li>
<li>Change the template code in <b>CF/dist/template.cpp</b> as it suits you. (Let the end-comment be there to show support <b>:)</b> ).</li>

</ol>



<a name="usage"><h3>Usage</h3></a>
<ul>
<li>After the installation, you should see a new menu in the menu bar, <b>Buggy</b>.</li>
<li>Click on the <b>Buggy</b> menu and you&#39;ll be able to see all the options there.
	<ul>
	<li>If you are not able to see all the options, <b>"Tools -> Build System"</b> and select <b>CF</b>.</li>
	</ul>
</li>
<li>Make sure Sublime Side-Bar is visible (<b>View -> Side Bar -> Show Side Bar</b>).</li>
<li>To start parsing the test-cases, <b>(Buggy -> Start)</b>.</li>
<li>For parsing the test-cases, provide the round-number you see in the url of the contest.</li>
<li>Compile the code before running it on test-cases (<b>Ctrl+B</b> or <b>Buggy -> Compile</b>)</li>
<li>Copy the code before going to submit the code.</li>
<li>If you want you can change the key-bindings too.</li>
<li>If you are working behind proxy
	<ul>
	<li>Open dist/proxy.txt</li>
	<li>Delete all the contents of the file and add your proxy with the following format </li>
	<li>username:password@proxy:port</li>
	</ul>
</li>
<li>If you want the problem-set to open in your default browser, uncomment the last two lines of <b>CF/dist/start.sh</b> </li>
</ul>
<center><img src="https://github.com/pakhandi/Buggy---Linux/blob/master/src_linux/menu.jpg?raw=true"></center>
<br>
<center><img src="https://github.com/pakhandi/Buggy---Linux/blob/master/src_linux/CF.JPG?raw=true"></center>
<br><br>


<a name="techused"><h3>Technology Used</h3></a>
<ul>
<li>The application is made using Python-2.7.9 and Shell scripting</li>
<li><b>BeautifulSoup</b> module is used alongwith <b>requests</b> in Python</li>
<li>Executables are made using cx_freeze</li>
</ul>

<a name="testing"><h3>Testing</h3></a>
The program has been tested on Ubuntu14.04, 64-bit

<br>
Refer to <a href="http://bugecode.com/post.php?pid=118" target="_blank">this post</a> for more detailed explanation of the working of the application.
<br>
<br>
For Hugs and Bugs drop a mail at <b>asimkprasad@gmail.com</b>

