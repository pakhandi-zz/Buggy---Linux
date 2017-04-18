<h1>Buggy : V.5.0 (Unstable)</h1>

<b>Download the stable version from <a href="http://pakhandi.github.io/Buggy---Linux/">here</a></b>

A sublime plug-in for CodeForces
<br /><br />
This application is to assist a competitive-programmer in a CodeForces round. This application downloads all the sample test cases for a problem and runs a user&#39;s solution program on all these test cases so that no time is wasted on manual checking of the solution.
<br />
The plugin now also comes with a terminal tool which can be used to test a solution on multiple input files. This terminal tool may prove useful to problem setters.
<br />
<b>NOTE : </b>Please try the Plug-in once before using it in actual contest to avoid any last minute confusions.<br />
<b>Make Sure you have read <a href="#installation">Installation</a> and <a href="#usage">Usage</a> very very carefully.</b>
<br>

<h3>Index</h3>
<ol>
<li><a href="#requisites">Requisites</a></li>
<li><a href="#installation">Installation</a></li>
<li><a href="#usage">Usage</a></li>
<li><a href="#advusage">Advanced Usage (from terminal)</a></li>
<li><a href="#techused">Technology Used</a></li>
<li><a href="#testing">Testing</a></li>
<li><a href="#uninstall">Un-installation</a></li>
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
</ul>

<a name="installation"><h3>Installation</h3></a>
<ol>
<li>Download all the files from <a href="http://pakhandi.github.io/Buggy---Linux/">here</a>.</li>
<li>Run <b>sudo ./install</b> in the extracted directory.</li>
<li>Open sublime. GoTo <b>"Tools -> Build System"</b> and select <b>Buggy-C++</b> or <b>Buggy-JAVA</b></li>
<li>If you see <b>Buggy</b> menu in the menu-bar, installation is complete</li>
<li>Change the template code by <b>Buggy -> Template</b> as it suits you. (Let the end-comment be there to show support <b>:)</b> ).</li>

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
<li>Compile the code before running it on test-cases (<b>Ctrl+1</b> or <b>Buggy -> Compile</b>)</li>
<li>Copy the code before going to submit the code.</li>
<li>If you want you can change the key-bindings too.</li>
<li>If you are working behind proxy
	<ul>
	<li>Open <b>Buggy -> Config</b></li>
	<li>Enter your proxy information with format : proxyConfig: username:password@ip:port</li>
	</ul>
</li>
<li>To change the default directory for download
	<ul>
	<li>Open <b>Buggy -> Config</b></li>
	<li>Enter your default directory with format : path: ~/path/to/target/directory/</li>
	</ul>
</li>
</ul>
<center><img src="https://github.com/pakhandi/Buggy---Linux/blob/master/src_linux/menu.jpg?raw=true"></center>
<br>
<center><img src="https://github.com/pakhandi/Buggy---Linux/blob/master/src_linux/CF.JPG?raw=true"></center>
<br><br>

<a name="advusage"><h3>Advanced Usage (from terminal)</h3></a>
<ul>
<li>The c++ program is compiled with flag <b>-D BUGGY</b>. This enables users to use code-snippet like

```cpp
#ifdef BUGGY
	// something
#endif
```

<li>In Terminal use <b>BuggyBatchTest --help</b> to get details of usage from terminal.</li>
<li>Terminal usage allows to run an executable on multiple input files and compare the output against multiple corresponding output files.</li>
<li>The input files should have format <b>inPrefix</b><i>i</i><b>inSuffix</b>, where <i>i</i> is 0, 1, 2, ...</li>
<li>Similarly the output files should have format <b>outPrefix</b><i>i</i><b>outSuffix</b>, where <i>i</i> is 0, 1, 2, ...</li>
<li>
	For example, in the case where :
	<ul>
	<li>All input files are of format : in<i>i</i>.txt</li>
	<li>Input files are in the directory inputFiles</li>
	<li>Name of the executable is aprog</li>
	<li>All the output files are of format : out<i>i</i>.txt</li>
	<li>Output files are in the same directory from where the command is being run (in this case assumed to be the same directory as the executable)</li>
	<li>Language used is C++</li>
	<li>And we just want to see the verdict with colors</li>
	</ul>
	The command will be structured as :
	<b>BuggyBatchTest --inPrefix in --inSuffix .txt --inPath inputFiles/ -f aprog --outPrefix out --outSuffix .txt -l cpp -c</b>
</li>
<li>For example , all input files are of format : in<i>i</i>.txt and these files are in directory : inputFiles, and name of the executable is aprog, then the command will be structured as : <b>BuggyBatchtest --inPrefix in --inSuffix .txt --inPath inputFiles -f aprog -l cpp</b></li>
</ul>

<a name="techused"><h3>Technology Used</h3></a>
<ul>
<li>The application is made using Python-2.7.9 and Shell scripting</li>
<li><b>BeautifulSoup</b> module is used in Python</li>
<li>Executables are made using cx_freeze</li>
</ul>

<a name="testing"><h3>Testing</h3></a>
The program has been tested on Ubuntu-14.04, 64-bit

<a name="uninstall"><h3>Un-installation</h3></a>
<ol>
<li>Download all the files from <a href="http://pakhandi.github.io/Buggy---Linux/">here</a>.</li>
<li>Run <b>sudo ./unInstall</b> in the extracted directory.</li>
</ol>

<br>
Refer to <a href="http://bugecode.com/post.php?pid=118" target="_blank">this post</a> for more detailed explanation of the working of the application.
<br>
<br>
For Hugs and Bugs drop a mail at <b>asimkprasad@gmail.com</b>
