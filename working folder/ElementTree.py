<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en-US">
<head>
<link rel="icon" href="/cpython/static/hgicon.png" type="image/png" />
<meta name="robots" content="index, nofollow" />
<link rel="stylesheet" href="/cpython/static/style-paper.css" type="text/css" />
<script type="text/javascript" src="/cpython/static/mercurial.js"></script>

<link rel="stylesheet" href="/cpython/highlightcss" type="text/css" />
<title>cpython: 7ba47bbfe38d Lib/xml/etree/ElementTree.py</title>
</head>
<body>

<div class="container">
<div class="menu">
<div class="logo">
<a href="https://hg.python.org">
<img src="/cpython/static/hglogo.png" alt="back to hg.python.org repositories" /></a>
</div>
<ul>
<li><a href="/cpython/shortlog/7ba47bbfe38d">log</a></li>
<li><a href="/cpython/graph/7ba47bbfe38d">graph</a></li>
<li><a href="/cpython/tags">tags</a></li>
<li><a href="/cpython/branches">branches</a></li>
</ul>
<ul>
<li><a href="/cpython/rev/7ba47bbfe38d">changeset</a></li>
<li><a href="/cpython/file/7ba47bbfe38d/Lib/xml/etree/">browse</a></li>
</ul>
<ul>
<li class="active">file</li>
<li><a href="/cpython/file/tip/Lib/xml/etree/ElementTree.py">latest</a></li>
<li><a href="/cpython/diff/7ba47bbfe38d/Lib/xml/etree/ElementTree.py">diff</a></li>
<li><a href="/cpython/comparison/7ba47bbfe38d/Lib/xml/etree/ElementTree.py">comparison</a></li>
<li><a href="/cpython/annotate/7ba47bbfe38d/Lib/xml/etree/ElementTree.py">annotate</a></li>
<li><a href="/cpython/log/7ba47bbfe38d/Lib/xml/etree/ElementTree.py">file log</a></li>
<li><a href="/cpython/raw-file/7ba47bbfe38d/Lib/xml/etree/ElementTree.py">raw</a></li>
</ul>
<ul>
<li><a href="/cpython/help">help</a></li>
</ul>
</div>

<div class="main">
<h2 class="breadcrumb"><a href="/">Mercurial</a> &gt; <a href="/cpython">cpython</a> </h2>
<h3>view Lib/xml/etree/ElementTree.py @ 93060:7ba47bbfe38d</h3>

<form class="search" action="/cpython/log">

<p><input name="rev" id="search1" type="text" size="30" /></p>
<div id="hint">Find changesets by keywords (author, files, the commit message), revision
number or hash, or <a href="/cpython/help/revsets">revset expression</a>.</div>
</form>

<div class="description">Issue #3068: Change 0/1 to False/True so that extension configure dialog can
easily recognize and display boolean values as such and recognize changes.
Also reformat comments and alphabetize extensions included with Idle.</a> [<a href="http://bugs.python.org/3068" class="issuelink">#3068</a>]</div>

<table id="changesetEntry">
<tr>
 <th class="author">author</th>
 <td class="author">&#84;&#101;&#114;&#114;&#121;&#32;&#74;&#97;&#110;&#32;&#82;&#101;&#101;&#100;&#121;&#32;&#60;&#116;&#106;&#114;&#101;&#101;&#100;&#121;&#64;&#117;&#100;&#101;&#108;&#46;&#101;&#100;&#117;&#62;</td>
</tr>
<tr>
 <th class="date">date</th>
 <td class="date age">Tue, 14 Oct 2014 18:55:13 -0400</td>
</tr>
<tr>
 <th class="author">parents</th>
 <td class="author"><a href="/cpython/file/8e6db2462a77/Lib/xml/etree/ElementTree.py">8e6db2462a77</a> </td>
</tr>
<tr>
 <th class="author">children</th>
 <td class="author"></td>
</tr>
</table>

<div class="overflow">
<div class="sourcefirst linewraptoggle">line wrap: <a class="linewraplink" href="javascript:toggleLinewrap()">on</a></div>
<div class="sourcefirst"> line source</div>
<pre class="sourcelines stripes4 wrap">
<span id="l1"><span class="c">#</span></span><a href="#l1"></a>
<span id="l2"><span class="c"># ElementTree</span></span><a href="#l2"></a>
<span id="l3"><span class="c"># $Id: ElementTree.py 3440 2008-07-18 14:45:01Z fredrik $</span></span><a href="#l3"></a>
<span id="l4"><span class="c">#</span></span><a href="#l4"></a>
<span id="l5"><span class="c"># light-weight XML support for Python 2.3 and later.</span></span><a href="#l5"></a>
<span id="l6"><span class="c">#</span></span><a href="#l6"></a>
<span id="l7"><span class="c"># history (since 1.2.6):</span></span><a href="#l7"></a>
<span id="l8"><span class="c"># 2005-11-12 fl   added tostringlist/fromstringlist helpers</span></span><a href="#l8"></a>
<span id="l9"><span class="c"># 2006-07-05 fl   merged in selected changes from the 1.3 sandbox</span></span><a href="#l9"></a>
<span id="l10"><span class="c"># 2006-07-05 fl   removed support for 2.1 and earlier</span></span><a href="#l10"></a>
<span id="l11"><span class="c"># 2007-06-21 fl   added deprecation/future warnings</span></span><a href="#l11"></a>
<span id="l12"><span class="c"># 2007-08-25 fl   added doctype hook, added parser version attribute etc</span></span><a href="#l12"></a>
<span id="l13"><span class="c"># 2007-08-26 fl   added new serializer code (better namespace handling, etc)</span></span><a href="#l13"></a>
<span id="l14"><span class="c"># 2007-08-27 fl   warn for broken /tag searches on tree level</span></span><a href="#l14"></a>
<span id="l15"><span class="c"># 2007-09-02 fl   added html/text methods to serializer (experimental)</span></span><a href="#l15"></a>
<span id="l16"><span class="c"># 2007-09-05 fl   added method argument to tostring/tostringlist</span></span><a href="#l16"></a>
<span id="l17"><span class="c"># 2007-09-06 fl   improved error handling</span></span><a href="#l17"></a>
<span id="l18"><span class="c"># 2007-09-13 fl   added itertext, iterfind; assorted cleanups</span></span><a href="#l18"></a>
<span id="l19"><span class="c"># 2007-12-15 fl   added C14N hooks, copy method (experimental)</span></span><a href="#l19"></a>
<span id="l20"><span class="c">#</span></span><a href="#l20"></a>
<span id="l21"><span class="c"># Copyright (c) 1999-2008 by Fredrik Lundh.  All rights reserved.</span></span><a href="#l21"></a>
<span id="l22"><span class="c">#</span></span><a href="#l22"></a>
<span id="l23"><span class="c"># fredrik@pythonware.com</span></span><a href="#l23"></a>
<span id="l24"><span class="c"># http://www.pythonware.com</span></span><a href="#l24"></a>
<span id="l25"><span class="c">#</span></span><a href="#l25"></a>
<span id="l26"><span class="c"># --------------------------------------------------------------------</span></span><a href="#l26"></a>
<span id="l27"><span class="c"># The ElementTree toolkit is</span></span><a href="#l27"></a>
<span id="l28"><span class="c">#</span></span><a href="#l28"></a>
<span id="l29"><span class="c"># Copyright (c) 1999-2008 by Fredrik Lundh</span></span><a href="#l29"></a>
<span id="l30"><span class="c">#</span></span><a href="#l30"></a>
<span id="l31"><span class="c"># By obtaining, using, and/or copying this software and/or its</span></span><a href="#l31"></a>
<span id="l32"><span class="c"># associated documentation, you agree that you have read, understood,</span></span><a href="#l32"></a>
<span id="l33"><span class="c"># and will comply with the following terms and conditions:</span></span><a href="#l33"></a>
<span id="l34"><span class="c">#</span></span><a href="#l34"></a>
<span id="l35"><span class="c"># Permission to use, copy, modify, and distribute this software and</span></span><a href="#l35"></a>
<span id="l36"><span class="c"># its associated documentation for any purpose and without fee is</span></span><a href="#l36"></a>
<span id="l37"><span class="c"># hereby granted, provided that the above copyright notice appears in</span></span><a href="#l37"></a>
<span id="l38"><span class="c"># all copies, and that both that copyright notice and this permission</span></span><a href="#l38"></a>
<span id="l39"><span class="c"># notice appear in supporting documentation, and that the name of</span></span><a href="#l39"></a>
<span id="l40"><span class="c"># Secret Labs AB or the author not be used in advertising or publicity</span></span><a href="#l40"></a>
<span id="l41"><span class="c"># pertaining to distribution of the software without specific, written</span></span><a href="#l41"></a>
<span id="l42"><span class="c"># prior permission.</span></span><a href="#l42"></a>
<span id="l43"><span class="c">#</span></span><a href="#l43"></a>
<span id="l44"><span class="c"># SECRET LABS AB AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD</span></span><a href="#l44"></a>
<span id="l45"><span class="c"># TO THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANT-</span></span><a href="#l45"></a>
<span id="l46"><span class="c"># ABILITY AND FITNESS.  IN NO EVENT SHALL SECRET LABS AB OR THE AUTHOR</span></span><a href="#l46"></a>
<span id="l47"><span class="c"># BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY</span></span><a href="#l47"></a>
<span id="l48"><span class="c"># DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS,</span></span><a href="#l48"></a>
<span id="l49"><span class="c"># WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS</span></span><a href="#l49"></a>
<span id="l50"><span class="c"># ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE</span></span><a href="#l50"></a>
<span id="l51"><span class="c"># OF THIS SOFTWARE.</span></span><a href="#l51"></a>
<span id="l52"><span class="c"># --------------------------------------------------------------------</span></span><a href="#l52"></a>
<span id="l53"></span><a href="#l53"></a>
<span id="l54"><span class="c"># Licensed to PSF under a Contributor Agreement.</span></span><a href="#l54"></a>
<span id="l55"><span class="c"># See http://www.python.org/psf/license for licensing details.</span></span><a href="#l55"></a>
<span id="l56"></span><a href="#l56"></a>
<span id="l57"><span class="n">__all__</span> <span class="o">=</span> <span class="p">[</span></span><a href="#l57"></a>
<span id="l58">    <span class="c"># public symbols</span></span><a href="#l58"></a>
<span id="l59">    <span class="s">&quot;Comment&quot;</span><span class="p">,</span></span><a href="#l59"></a>
<span id="l60">    <span class="s">&quot;dump&quot;</span><span class="p">,</span></span><a href="#l60"></a>
<span id="l61">    <span class="s">&quot;Element&quot;</span><span class="p">,</span> <span class="s">&quot;ElementTree&quot;</span><span class="p">,</span></span><a href="#l61"></a>
<span id="l62">    <span class="s">&quot;fromstring&quot;</span><span class="p">,</span> <span class="s">&quot;fromstringlist&quot;</span><span class="p">,</span></span><a href="#l62"></a>
<span id="l63">    <span class="s">&quot;iselement&quot;</span><span class="p">,</span> <span class="s">&quot;iterparse&quot;</span><span class="p">,</span></span><a href="#l63"></a>
<span id="l64">    <span class="s">&quot;parse&quot;</span><span class="p">,</span> <span class="s">&quot;ParseError&quot;</span><span class="p">,</span></span><a href="#l64"></a>
<span id="l65">    <span class="s">&quot;PI&quot;</span><span class="p">,</span> <span class="s">&quot;ProcessingInstruction&quot;</span><span class="p">,</span></span><a href="#l65"></a>
<span id="l66">    <span class="s">&quot;QName&quot;</span><span class="p">,</span></span><a href="#l66"></a>
<span id="l67">    <span class="s">&quot;SubElement&quot;</span><span class="p">,</span></span><a href="#l67"></a>
<span id="l68">    <span class="s">&quot;tostring&quot;</span><span class="p">,</span> <span class="s">&quot;tostringlist&quot;</span><span class="p">,</span></span><a href="#l68"></a>
<span id="l69">    <span class="s">&quot;TreeBuilder&quot;</span><span class="p">,</span></span><a href="#l69"></a>
<span id="l70">    <span class="s">&quot;VERSION&quot;</span><span class="p">,</span></span><a href="#l70"></a>
<span id="l71">    <span class="s">&quot;XML&quot;</span><span class="p">,</span></span><a href="#l71"></a>
<span id="l72">    <span class="s">&quot;XMLParser&quot;</span><span class="p">,</span> <span class="s">&quot;XMLTreeBuilder&quot;</span><span class="p">,</span></span><a href="#l72"></a>
<span id="l73">    <span class="p">]</span></span><a href="#l73"></a>
<span id="l74"></span><a href="#l74"></a>
<span id="l75"><span class="n">VERSION</span> <span class="o">=</span> <span class="s">&quot;1.3.0&quot;</span></span><a href="#l75"></a>
<span id="l76"></span><a href="#l76"></a>
<span id="l77"><span class="c">##</span></span><a href="#l77"></a>
<span id="l78"><span class="c"># The &lt;b&gt;Element&lt;/b&gt; type is a flexible container object, designed to</span></span><a href="#l78"></a>
<span id="l79"><span class="c"># store hierarchical data structures in memory. The type can be</span></span><a href="#l79"></a>
<span id="l80"><span class="c"># described as a cross between a list and a dictionary.</span></span><a href="#l80"></a>
<span id="l81"><span class="c"># &lt;p&gt;</span></span><a href="#l81"></a>
<span id="l82"><span class="c"># Each element has a number of properties associated with it:</span></span><a href="#l82"></a>
<span id="l83"><span class="c"># &lt;ul&gt;</span></span><a href="#l83"></a>
<span id="l84"><span class="c"># &lt;li&gt;a &lt;i&gt;tag&lt;/i&gt;. This is a string identifying what kind of data</span></span><a href="#l84"></a>
<span id="l85"><span class="c"># this element represents (the element type, in other words).&lt;/li&gt;</span></span><a href="#l85"></a>
<span id="l86"><span class="c"># &lt;li&gt;a number of &lt;i&gt;attributes&lt;/i&gt;, stored in a Python dictionary.&lt;/li&gt;</span></span><a href="#l86"></a>
<span id="l87"><span class="c"># &lt;li&gt;a &lt;i&gt;text&lt;/i&gt; string.&lt;/li&gt;</span></span><a href="#l87"></a>
<span id="l88"><span class="c"># &lt;li&gt;an optional &lt;i&gt;tail&lt;/i&gt; string.&lt;/li&gt;</span></span><a href="#l88"></a>
<span id="l89"><span class="c"># &lt;li&gt;a number of &lt;i&gt;child elements&lt;/i&gt;, stored in a Python sequence&lt;/li&gt;</span></span><a href="#l89"></a>
<span id="l90"><span class="c"># &lt;/ul&gt;</span></span><a href="#l90"></a>
<span id="l91"><span class="c">#</span></span><a href="#l91"></a>
<span id="l92"><span class="c"># To create an element instance, use the {@link #Element} constructor</span></span><a href="#l92"></a>
<span id="l93"><span class="c"># or the {@link #SubElement} factory function.</span></span><a href="#l93"></a>
<span id="l94"><span class="c"># &lt;p&gt;</span></span><a href="#l94"></a>
<span id="l95"><span class="c"># The {@link #ElementTree} class can be used to wrap an element</span></span><a href="#l95"></a>
<span id="l96"><span class="c"># structure, and convert it from and to XML.</span></span><a href="#l96"></a>
<span id="l97"><span class="c">##</span></span><a href="#l97"></a>
<span id="l98"></span><a href="#l98"></a>
<span id="l99"><span class="kn">import</span> <span class="nn">sys</span></span><a href="#l99"></a>
<span id="l100"><span class="kn">import</span> <span class="nn">re</span></span><a href="#l100"></a>
<span id="l101"><span class="kn">import</span> <span class="nn">warnings</span></span><a href="#l101"></a>
<span id="l102"></span><a href="#l102"></a>
<span id="l103"></span><a href="#l103"></a>
<span id="l104"><span class="k">class</span> <span class="nc">_SimpleElementPath</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></span><a href="#l104"></a>
<span id="l105">    <span class="c"># emulate pre-1.2 find/findtext/findall behaviour</span></span><a href="#l105"></a>
<span id="l106">    <span class="k">def</span> <span class="nf">find</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">element</span><span class="p">,</span> <span class="n">tag</span><span class="p">,</span> <span class="n">namespaces</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l106"></a>
<span id="l107">        <span class="k">for</span> <span class="n">elem</span> <span class="ow">in</span> <span class="n">element</span><span class="p">:</span></span><a href="#l107"></a>
<span id="l108">            <span class="k">if</span> <span class="n">elem</span><span class="o">.</span><span class="n">tag</span> <span class="o">==</span> <span class="n">tag</span><span class="p">:</span></span><a href="#l108"></a>
<span id="l109">                <span class="k">return</span> <span class="n">elem</span></span><a href="#l109"></a>
<span id="l110">        <span class="k">return</span> <span class="bp">None</span></span><a href="#l110"></a>
<span id="l111">    <span class="k">def</span> <span class="nf">findtext</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">element</span><span class="p">,</span> <span class="n">tag</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">namespaces</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l111"></a>
<span id="l112">        <span class="n">elem</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="n">element</span><span class="p">,</span> <span class="n">tag</span><span class="p">)</span></span><a href="#l112"></a>
<span id="l113">        <span class="k">if</span> <span class="n">elem</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l113"></a>
<span id="l114">            <span class="k">return</span> <span class="n">default</span></span><a href="#l114"></a>
<span id="l115">        <span class="k">return</span> <span class="n">elem</span><span class="o">.</span><span class="n">text</span> <span class="ow">or</span> <span class="s">&quot;&quot;</span></span><a href="#l115"></a>
<span id="l116">    <span class="k">def</span> <span class="nf">iterfind</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">element</span><span class="p">,</span> <span class="n">tag</span><span class="p">,</span> <span class="n">namespaces</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l116"></a>
<span id="l117">        <span class="k">if</span> <span class="n">tag</span><span class="p">[:</span><span class="mi">3</span><span class="p">]</span> <span class="o">==</span> <span class="s">&quot;.//&quot;</span><span class="p">:</span></span><a href="#l117"></a>
<span id="l118">            <span class="k">for</span> <span class="n">elem</span> <span class="ow">in</span> <span class="n">element</span><span class="o">.</span><span class="n">iter</span><span class="p">(</span><span class="n">tag</span><span class="p">[</span><span class="mi">3</span><span class="p">:]):</span></span><a href="#l118"></a>
<span id="l119">                <span class="k">yield</span> <span class="n">elem</span></span><a href="#l119"></a>
<span id="l120">        <span class="k">for</span> <span class="n">elem</span> <span class="ow">in</span> <span class="n">element</span><span class="p">:</span></span><a href="#l120"></a>
<span id="l121">            <span class="k">if</span> <span class="n">elem</span><span class="o">.</span><span class="n">tag</span> <span class="o">==</span> <span class="n">tag</span><span class="p">:</span></span><a href="#l121"></a>
<span id="l122">                <span class="k">yield</span> <span class="n">elem</span></span><a href="#l122"></a>
<span id="l123">    <span class="k">def</span> <span class="nf">findall</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">element</span><span class="p">,</span> <span class="n">tag</span><span class="p">,</span> <span class="n">namespaces</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l123"></a>
<span id="l124">        <span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">iterfind</span><span class="p">(</span><span class="n">element</span><span class="p">,</span> <span class="n">tag</span><span class="p">,</span> <span class="n">namespaces</span><span class="p">))</span></span><a href="#l124"></a>
<span id="l125"></span><a href="#l125"></a>
<span id="l126"><span class="k">try</span><span class="p">:</span></span><a href="#l126"></a>
<span id="l127">    <span class="kn">from</span> <span class="nn">.</span> <span class="kn">import</span> <span class="n">ElementPath</span></span><a href="#l127"></a>
<span id="l128"><span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span></span><a href="#l128"></a>
<span id="l129">    <span class="n">ElementPath</span> <span class="o">=</span> <span class="n">_SimpleElementPath</span><span class="p">()</span></span><a href="#l129"></a>
<span id="l130"></span><a href="#l130"></a>
<span id="l131"><span class="c">##</span></span><a href="#l131"></a>
<span id="l132"><span class="c"># Parser error.  This is a subclass of &lt;b&gt;SyntaxError&lt;/b&gt;.</span></span><a href="#l132"></a>
<span id="l133"><span class="c"># &lt;p&gt;</span></span><a href="#l133"></a>
<span id="l134"><span class="c"># In addition to the exception value, an exception instance contains a</span></span><a href="#l134"></a>
<span id="l135"><span class="c"># specific exception code in the &lt;b&gt;code&lt;/b&gt; attribute, and the line and</span></span><a href="#l135"></a>
<span id="l136"><span class="c"># column of the error in the &lt;b&gt;position&lt;/b&gt; attribute.</span></span><a href="#l136"></a>
<span id="l137"></span><a href="#l137"></a>
<span id="l138"><span class="k">class</span> <span class="nc">ParseError</span><span class="p">(</span><span class="ne">SyntaxError</span><span class="p">):</span></span><a href="#l138"></a>
<span id="l139">    <span class="k">pass</span></span><a href="#l139"></a>
<span id="l140"></span><a href="#l140"></a>
<span id="l141"><span class="c"># --------------------------------------------------------------------</span></span><a href="#l141"></a>
<span id="l142"></span><a href="#l142"></a>
<span id="l143"><span class="c">##</span></span><a href="#l143"></a>
<span id="l144"><span class="c"># Checks if an object appears to be a valid element object.</span></span><a href="#l144"></a>
<span id="l145"><span class="c">#</span></span><a href="#l145"></a>
<span id="l146"><span class="c"># @param An element instance.</span></span><a href="#l146"></a>
<span id="l147"><span class="c"># @return A true value if this is an element object.</span></span><a href="#l147"></a>
<span id="l148"><span class="c"># @defreturn flag</span></span><a href="#l148"></a>
<span id="l149"></span><a href="#l149"></a>
<span id="l150"><span class="k">def</span> <span class="nf">iselement</span><span class="p">(</span><span class="n">element</span><span class="p">):</span></span><a href="#l150"></a>
<span id="l151">    <span class="c"># FIXME: not sure about this; might be a better idea to look</span></span><a href="#l151"></a>
<span id="l152">    <span class="c"># for tag/attrib/text attributes</span></span><a href="#l152"></a>
<span id="l153">    <span class="k">return</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">element</span><span class="p">,</span> <span class="n">Element</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">element</span><span class="p">,</span> <span class="s">&quot;tag&quot;</span><span class="p">)</span></span><a href="#l153"></a>
<span id="l154"></span><a href="#l154"></a>
<span id="l155"><span class="c">##</span></span><a href="#l155"></a>
<span id="l156"><span class="c"># Element class.  This class defines the Element interface, and</span></span><a href="#l156"></a>
<span id="l157"><span class="c"># provides a reference implementation of this interface.</span></span><a href="#l157"></a>
<span id="l158"><span class="c"># &lt;p&gt;</span></span><a href="#l158"></a>
<span id="l159"><span class="c"># The element name, attribute names, and attribute values can be</span></span><a href="#l159"></a>
<span id="l160"><span class="c"># either ASCII strings (ordinary Python strings containing only 7-bit</span></span><a href="#l160"></a>
<span id="l161"><span class="c"># ASCII characters) or Unicode strings.</span></span><a href="#l161"></a>
<span id="l162"><span class="c">#</span></span><a href="#l162"></a>
<span id="l163"><span class="c"># @param tag The element name.</span></span><a href="#l163"></a>
<span id="l164"><span class="c"># @param attrib An optional dictionary, containing element attributes.</span></span><a href="#l164"></a>
<span id="l165"><span class="c"># @param **extra Additional attributes, given as keyword arguments.</span></span><a href="#l165"></a>
<span id="l166"><span class="c"># @see Element</span></span><a href="#l166"></a>
<span id="l167"><span class="c"># @see SubElement</span></span><a href="#l167"></a>
<span id="l168"><span class="c"># @see Comment</span></span><a href="#l168"></a>
<span id="l169"><span class="c"># @see ProcessingInstruction</span></span><a href="#l169"></a>
<span id="l170"></span><a href="#l170"></a>
<span id="l171"><span class="k">class</span> <span class="nc">Element</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></span><a href="#l171"></a>
<span id="l172">    <span class="c"># &lt;tag attrib&gt;text&lt;child/&gt;...&lt;/tag&gt;tail</span></span><a href="#l172"></a>
<span id="l173"></span><a href="#l173"></a>
<span id="l174">    <span class="c">##</span></span><a href="#l174"></a>
<span id="l175">    <span class="c"># (Attribute) Element tag.</span></span><a href="#l175"></a>
<span id="l176"></span><a href="#l176"></a>
<span id="l177">    <span class="n">tag</span> <span class="o">=</span> <span class="bp">None</span></span><a href="#l177"></a>
<span id="l178"></span><a href="#l178"></a>
<span id="l179">    <span class="c">##</span></span><a href="#l179"></a>
<span id="l180">    <span class="c"># (Attribute) Element attribute dictionary.  Where possible, use</span></span><a href="#l180"></a>
<span id="l181">    <span class="c"># {@link #Element.get},</span></span><a href="#l181"></a>
<span id="l182">    <span class="c"># {@link #Element.set},</span></span><a href="#l182"></a>
<span id="l183">    <span class="c"># {@link #Element.keys}, and</span></span><a href="#l183"></a>
<span id="l184">    <span class="c"># {@link #Element.items} to access</span></span><a href="#l184"></a>
<span id="l185">    <span class="c"># element attributes.</span></span><a href="#l185"></a>
<span id="l186"></span><a href="#l186"></a>
<span id="l187">    <span class="n">attrib</span> <span class="o">=</span> <span class="bp">None</span></span><a href="#l187"></a>
<span id="l188"></span><a href="#l188"></a>
<span id="l189">    <span class="c">##</span></span><a href="#l189"></a>
<span id="l190">    <span class="c"># (Attribute) Text before first subelement.  This is either a</span></span><a href="#l190"></a>
<span id="l191">    <span class="c"># string or the value None.  Note that if there was no text, this</span></span><a href="#l191"></a>
<span id="l192">    <span class="c"># attribute may be either None or an empty string, depending on</span></span><a href="#l192"></a>
<span id="l193">    <span class="c"># the parser.</span></span><a href="#l193"></a>
<span id="l194"></span><a href="#l194"></a>
<span id="l195">    <span class="n">text</span> <span class="o">=</span> <span class="bp">None</span></span><a href="#l195"></a>
<span id="l196"></span><a href="#l196"></a>
<span id="l197">    <span class="c">##</span></span><a href="#l197"></a>
<span id="l198">    <span class="c"># (Attribute) Text after this element&#39;s end tag, but before the</span></span><a href="#l198"></a>
<span id="l199">    <span class="c"># next sibling element&#39;s start tag.  This is either a string or</span></span><a href="#l199"></a>
<span id="l200">    <span class="c"># the value None.  Note that if there was no text, this attribute</span></span><a href="#l200"></a>
<span id="l201">    <span class="c"># may be either None or an empty string, depending on the parser.</span></span><a href="#l201"></a>
<span id="l202"></span><a href="#l202"></a>
<span id="l203">    <span class="n">tail</span> <span class="o">=</span> <span class="bp">None</span> <span class="c"># text after end tag, if any</span></span><a href="#l203"></a>
<span id="l204"></span><a href="#l204"></a>
<span id="l205">    <span class="c"># constructor</span></span><a href="#l205"></a>
<span id="l206"></span><a href="#l206"></a>
<span id="l207">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tag</span><span class="p">,</span> <span class="n">attrib</span><span class="o">=</span><span class="p">{},</span> <span class="o">**</span><span class="n">extra</span><span class="p">):</span></span><a href="#l207"></a>
<span id="l208">        <span class="n">attrib</span> <span class="o">=</span> <span class="n">attrib</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span></span><a href="#l208"></a>
<span id="l209">        <span class="n">attrib</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">extra</span><span class="p">)</span></span><a href="#l209"></a>
<span id="l210">        <span class="bp">self</span><span class="o">.</span><span class="n">tag</span> <span class="o">=</span> <span class="n">tag</span></span><a href="#l210"></a>
<span id="l211">        <span class="bp">self</span><span class="o">.</span><span class="n">attrib</span> <span class="o">=</span> <span class="n">attrib</span></span><a href="#l211"></a>
<span id="l212">        <span class="bp">self</span><span class="o">.</span><span class="n">_children</span> <span class="o">=</span> <span class="p">[]</span></span><a href="#l212"></a>
<span id="l213"></span><a href="#l213"></a>
<span id="l214">    <span class="k">def</span> <span class="nf">__repr__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l214"></a>
<span id="l215">        <span class="k">return</span> <span class="s">&quot;&lt;Element </span><span class="si">%s</span><span class="s"> at 0x</span><span class="si">%x</span><span class="s">&gt;&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="nb">repr</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">tag</span><span class="p">),</span> <span class="nb">id</span><span class="p">(</span><span class="bp">self</span><span class="p">))</span></span><a href="#l215"></a>
<span id="l216"></span><a href="#l216"></a>
<span id="l217">    <span class="c">##</span></span><a href="#l217"></a>
<span id="l218">    <span class="c"># Creates a new element object of the same type as this element.</span></span><a href="#l218"></a>
<span id="l219">    <span class="c">#</span></span><a href="#l219"></a>
<span id="l220">    <span class="c"># @param tag Element tag.</span></span><a href="#l220"></a>
<span id="l221">    <span class="c"># @param attrib Element attributes, given as a dictionary.</span></span><a href="#l221"></a>
<span id="l222">    <span class="c"># @return A new element instance.</span></span><a href="#l222"></a>
<span id="l223"></span><a href="#l223"></a>
<span id="l224">    <span class="k">def</span> <span class="nf">makeelement</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tag</span><span class="p">,</span> <span class="n">attrib</span><span class="p">):</span></span><a href="#l224"></a>
<span id="l225">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">__class__</span><span class="p">(</span><span class="n">tag</span><span class="p">,</span> <span class="n">attrib</span><span class="p">)</span></span><a href="#l225"></a>
<span id="l226"></span><a href="#l226"></a>
<span id="l227">    <span class="c">##</span></span><a href="#l227"></a>
<span id="l228">    <span class="c"># (Experimental) Copies the current element.  This creates a</span></span><a href="#l228"></a>
<span id="l229">    <span class="c"># shallow copy; subelements will be shared with the original tree.</span></span><a href="#l229"></a>
<span id="l230">    <span class="c">#</span></span><a href="#l230"></a>
<span id="l231">    <span class="c"># @return A new element instance.</span></span><a href="#l231"></a>
<span id="l232"></span><a href="#l232"></a>
<span id="l233">    <span class="k">def</span> <span class="nf">copy</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l233"></a>
<span id="l234">        <span class="n">elem</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">makeelement</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">tag</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">attrib</span><span class="p">)</span></span><a href="#l234"></a>
<span id="l235">        <span class="n">elem</span><span class="o">.</span><span class="n">text</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text</span></span><a href="#l235"></a>
<span id="l236">        <span class="n">elem</span><span class="o">.</span><span class="n">tail</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tail</span></span><a href="#l236"></a>
<span id="l237">        <span class="n">elem</span><span class="p">[:]</span> <span class="o">=</span> <span class="bp">self</span></span><a href="#l237"></a>
<span id="l238">        <span class="k">return</span> <span class="n">elem</span></span><a href="#l238"></a>
<span id="l239"></span><a href="#l239"></a>
<span id="l240">    <span class="c">##</span></span><a href="#l240"></a>
<span id="l241">    <span class="c"># Returns the number of subelements.  Note that this only counts</span></span><a href="#l241"></a>
<span id="l242">    <span class="c"># full elements; to check if there&#39;s any content in an element, you</span></span><a href="#l242"></a>
<span id="l243">    <span class="c"># have to check both the length and the &lt;b&gt;text&lt;/b&gt; attribute.</span></span><a href="#l243"></a>
<span id="l244">    <span class="c">#</span></span><a href="#l244"></a>
<span id="l245">    <span class="c"># @return The number of subelements.</span></span><a href="#l245"></a>
<span id="l246"></span><a href="#l246"></a>
<span id="l247">    <span class="k">def</span> <span class="nf">__len__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l247"></a>
<span id="l248">        <span class="k">return</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_children</span><span class="p">)</span></span><a href="#l248"></a>
<span id="l249"></span><a href="#l249"></a>
<span id="l250">    <span class="k">def</span> <span class="nf">__nonzero__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l250"></a>
<span id="l251">        <span class="n">warnings</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span></span><a href="#l251"></a>
<span id="l252">            <span class="s">&quot;The behavior of this method will change in future versions.  &quot;</span></span><a href="#l252"></a>
<span id="l253">            <span class="s">&quot;Use specific &#39;len(elem)&#39; or &#39;elem is not None&#39; test instead.&quot;</span><span class="p">,</span></span><a href="#l253"></a>
<span id="l254">            <span class="ne">FutureWarning</span><span class="p">,</span> <span class="n">stacklevel</span><span class="o">=</span><span class="mi">2</span></span><a href="#l254"></a>
<span id="l255">            <span class="p">)</span></span><a href="#l255"></a>
<span id="l256">        <span class="k">return</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_children</span><span class="p">)</span> <span class="o">!=</span> <span class="mi">0</span> <span class="c"># emulate old behaviour, for now</span></span><a href="#l256"></a>
<span id="l257"></span><a href="#l257"></a>
<span id="l258">    <span class="c">##</span></span><a href="#l258"></a>
<span id="l259">    <span class="c"># Returns the given subelement, by index.</span></span><a href="#l259"></a>
<span id="l260">    <span class="c">#</span></span><a href="#l260"></a>
<span id="l261">    <span class="c"># @param index What subelement to return.</span></span><a href="#l261"></a>
<span id="l262">    <span class="c"># @return The given subelement.</span></span><a href="#l262"></a>
<span id="l263">    <span class="c"># @exception IndexError If the given element does not exist.</span></span><a href="#l263"></a>
<span id="l264"></span><a href="#l264"></a>
<span id="l265">    <span class="k">def</span> <span class="nf">__getitem__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">index</span><span class="p">):</span></span><a href="#l265"></a>
<span id="l266">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_children</span><span class="p">[</span><span class="n">index</span><span class="p">]</span></span><a href="#l266"></a>
<span id="l267"></span><a href="#l267"></a>
<span id="l268">    <span class="c">##</span></span><a href="#l268"></a>
<span id="l269">    <span class="c"># Replaces the given subelement, by index.</span></span><a href="#l269"></a>
<span id="l270">    <span class="c">#</span></span><a href="#l270"></a>
<span id="l271">    <span class="c"># @param index What subelement to replace.</span></span><a href="#l271"></a>
<span id="l272">    <span class="c"># @param element The new element value.</span></span><a href="#l272"></a>
<span id="l273">    <span class="c"># @exception IndexError If the given element does not exist.</span></span><a href="#l273"></a>
<span id="l274"></span><a href="#l274"></a>
<span id="l275">    <span class="k">def</span> <span class="nf">__setitem__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">index</span><span class="p">,</span> <span class="n">element</span><span class="p">):</span></span><a href="#l275"></a>
<span id="l276">        <span class="c"># if isinstance(index, slice):</span></span><a href="#l276"></a>
<span id="l277">        <span class="c">#     for elt in element:</span></span><a href="#l277"></a>
<span id="l278">        <span class="c">#         assert iselement(elt)</span></span><a href="#l278"></a>
<span id="l279">        <span class="c"># else:</span></span><a href="#l279"></a>
<span id="l280">        <span class="c">#     assert iselement(element)</span></span><a href="#l280"></a>
<span id="l281">        <span class="bp">self</span><span class="o">.</span><span class="n">_children</span><span class="p">[</span><span class="n">index</span><span class="p">]</span> <span class="o">=</span> <span class="n">element</span></span><a href="#l281"></a>
<span id="l282"></span><a href="#l282"></a>
<span id="l283">    <span class="c">##</span></span><a href="#l283"></a>
<span id="l284">    <span class="c"># Deletes the given subelement, by index.</span></span><a href="#l284"></a>
<span id="l285">    <span class="c">#</span></span><a href="#l285"></a>
<span id="l286">    <span class="c"># @param index What subelement to delete.</span></span><a href="#l286"></a>
<span id="l287">    <span class="c"># @exception IndexError If the given element does not exist.</span></span><a href="#l287"></a>
<span id="l288"></span><a href="#l288"></a>
<span id="l289">    <span class="k">def</span> <span class="nf">__delitem__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">index</span><span class="p">):</span></span><a href="#l289"></a>
<span id="l290">        <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">_children</span><span class="p">[</span><span class="n">index</span><span class="p">]</span></span><a href="#l290"></a>
<span id="l291"></span><a href="#l291"></a>
<span id="l292">    <span class="c">##</span></span><a href="#l292"></a>
<span id="l293">    <span class="c"># Adds a subelement to the end of this element.  In document order,</span></span><a href="#l293"></a>
<span id="l294">    <span class="c"># the new element will appear after the last existing subelement (or</span></span><a href="#l294"></a>
<span id="l295">    <span class="c"># directly after the text, if it&#39;s the first subelement), but before</span></span><a href="#l295"></a>
<span id="l296">    <span class="c"># the end tag for this element.</span></span><a href="#l296"></a>
<span id="l297">    <span class="c">#</span></span><a href="#l297"></a>
<span id="l298">    <span class="c"># @param element The element to add.</span></span><a href="#l298"></a>
<span id="l299"></span><a href="#l299"></a>
<span id="l300">    <span class="k">def</span> <span class="nf">append</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">element</span><span class="p">):</span></span><a href="#l300"></a>
<span id="l301">        <span class="c"># assert iselement(element)</span></span><a href="#l301"></a>
<span id="l302">        <span class="bp">self</span><span class="o">.</span><span class="n">_children</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">element</span><span class="p">)</span></span><a href="#l302"></a>
<span id="l303"></span><a href="#l303"></a>
<span id="l304">    <span class="c">##</span></span><a href="#l304"></a>
<span id="l305">    <span class="c"># Appends subelements from a sequence.</span></span><a href="#l305"></a>
<span id="l306">    <span class="c">#</span></span><a href="#l306"></a>
<span id="l307">    <span class="c"># @param elements A sequence object with zero or more elements.</span></span><a href="#l307"></a>
<span id="l308">    <span class="c"># @since 1.3</span></span><a href="#l308"></a>
<span id="l309"></span><a href="#l309"></a>
<span id="l310">    <span class="k">def</span> <span class="nf">extend</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">elements</span><span class="p">):</span></span><a href="#l310"></a>
<span id="l311">        <span class="c"># for element in elements:</span></span><a href="#l311"></a>
<span id="l312">        <span class="c">#     assert iselement(element)</span></span><a href="#l312"></a>
<span id="l313">        <span class="bp">self</span><span class="o">.</span><span class="n">_children</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">elements</span><span class="p">)</span></span><a href="#l313"></a>
<span id="l314"></span><a href="#l314"></a>
<span id="l315">    <span class="c">##</span></span><a href="#l315"></a>
<span id="l316">    <span class="c"># Inserts a subelement at the given position in this element.</span></span><a href="#l316"></a>
<span id="l317">    <span class="c">#</span></span><a href="#l317"></a>
<span id="l318">    <span class="c"># @param index Where to insert the new subelement.</span></span><a href="#l318"></a>
<span id="l319"></span><a href="#l319"></a>
<span id="l320">    <span class="k">def</span> <span class="nf">insert</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">index</span><span class="p">,</span> <span class="n">element</span><span class="p">):</span></span><a href="#l320"></a>
<span id="l321">        <span class="c"># assert iselement(element)</span></span><a href="#l321"></a>
<span id="l322">        <span class="bp">self</span><span class="o">.</span><span class="n">_children</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="n">index</span><span class="p">,</span> <span class="n">element</span><span class="p">)</span></span><a href="#l322"></a>
<span id="l323"></span><a href="#l323"></a>
<span id="l324">    <span class="c">##</span></span><a href="#l324"></a>
<span id="l325">    <span class="c"># Removes a matching subelement.  Unlike the &lt;b&gt;find&lt;/b&gt; methods,</span></span><a href="#l325"></a>
<span id="l326">    <span class="c"># this method compares elements based on identity, not on tag</span></span><a href="#l326"></a>
<span id="l327">    <span class="c"># value or contents.  To remove subelements by other means, the</span></span><a href="#l327"></a>
<span id="l328">    <span class="c"># easiest way is often to use a list comprehension to select what</span></span><a href="#l328"></a>
<span id="l329">    <span class="c"># elements to keep, and use slice assignment to update the parent</span></span><a href="#l329"></a>
<span id="l330">    <span class="c"># element.</span></span><a href="#l330"></a>
<span id="l331">    <span class="c">#</span></span><a href="#l331"></a>
<span id="l332">    <span class="c"># @param element What element to remove.</span></span><a href="#l332"></a>
<span id="l333">    <span class="c"># @exception ValueError If a matching element could not be found.</span></span><a href="#l333"></a>
<span id="l334"></span><a href="#l334"></a>
<span id="l335">    <span class="k">def</span> <span class="nf">remove</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">element</span><span class="p">):</span></span><a href="#l335"></a>
<span id="l336">        <span class="c"># assert iselement(element)</span></span><a href="#l336"></a>
<span id="l337">        <span class="bp">self</span><span class="o">.</span><span class="n">_children</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">element</span><span class="p">)</span></span><a href="#l337"></a>
<span id="l338"></span><a href="#l338"></a>
<span id="l339">    <span class="c">##</span></span><a href="#l339"></a>
<span id="l340">    <span class="c"># (Deprecated) Returns all subelements.  The elements are returned</span></span><a href="#l340"></a>
<span id="l341">    <span class="c"># in document order.</span></span><a href="#l341"></a>
<span id="l342">    <span class="c">#</span></span><a href="#l342"></a>
<span id="l343">    <span class="c"># @return A list of subelements.</span></span><a href="#l343"></a>
<span id="l344">    <span class="c"># @defreturn list of Element instances</span></span><a href="#l344"></a>
<span id="l345"></span><a href="#l345"></a>
<span id="l346">    <span class="k">def</span> <span class="nf">getchildren</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l346"></a>
<span id="l347">        <span class="n">warnings</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span></span><a href="#l347"></a>
<span id="l348">            <span class="s">&quot;This method will be removed in future versions.  &quot;</span></span><a href="#l348"></a>
<span id="l349">            <span class="s">&quot;Use &#39;list(elem)&#39; or iteration over elem instead.&quot;</span><span class="p">,</span></span><a href="#l349"></a>
<span id="l350">            <span class="ne">DeprecationWarning</span><span class="p">,</span> <span class="n">stacklevel</span><span class="o">=</span><span class="mi">2</span></span><a href="#l350"></a>
<span id="l351">            <span class="p">)</span></span><a href="#l351"></a>
<span id="l352">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_children</span></span><a href="#l352"></a>
<span id="l353"></span><a href="#l353"></a>
<span id="l354">    <span class="c">##</span></span><a href="#l354"></a>
<span id="l355">    <span class="c"># Finds the first matching subelement, by tag name or path.</span></span><a href="#l355"></a>
<span id="l356">    <span class="c">#</span></span><a href="#l356"></a>
<span id="l357">    <span class="c"># @param path What element to look for.</span></span><a href="#l357"></a>
<span id="l358">    <span class="c"># @keyparam namespaces Optional namespace prefix map.</span></span><a href="#l358"></a>
<span id="l359">    <span class="c"># @return The first matching element, or None if no element was found.</span></span><a href="#l359"></a>
<span id="l360">    <span class="c"># @defreturn Element or None</span></span><a href="#l360"></a>
<span id="l361"></span><a href="#l361"></a>
<span id="l362">    <span class="k">def</span> <span class="nf">find</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">,</span> <span class="n">namespaces</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l362"></a>
<span id="l363">        <span class="k">return</span> <span class="n">ElementPath</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">,</span> <span class="n">namespaces</span><span class="p">)</span></span><a href="#l363"></a>
<span id="l364"></span><a href="#l364"></a>
<span id="l365">    <span class="c">##</span></span><a href="#l365"></a>
<span id="l366">    <span class="c"># Finds text for the first matching subelement, by tag name or path.</span></span><a href="#l366"></a>
<span id="l367">    <span class="c">#</span></span><a href="#l367"></a>
<span id="l368">    <span class="c"># @param path What element to look for.</span></span><a href="#l368"></a>
<span id="l369">    <span class="c"># @param default What to return if the element was not found.</span></span><a href="#l369"></a>
<span id="l370">    <span class="c"># @keyparam namespaces Optional namespace prefix map.</span></span><a href="#l370"></a>
<span id="l371">    <span class="c"># @return The text content of the first matching element, or the</span></span><a href="#l371"></a>
<span id="l372">    <span class="c">#     default value no element was found.  Note that if the element</span></span><a href="#l372"></a>
<span id="l373">    <span class="c">#     is found, but has no text content, this method returns an</span></span><a href="#l373"></a>
<span id="l374">    <span class="c">#     empty string.</span></span><a href="#l374"></a>
<span id="l375">    <span class="c"># @defreturn string</span></span><a href="#l375"></a>
<span id="l376"></span><a href="#l376"></a>
<span id="l377">    <span class="k">def</span> <span class="nf">findtext</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">namespaces</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l377"></a>
<span id="l378">        <span class="k">return</span> <span class="n">ElementPath</span><span class="o">.</span><span class="n">findtext</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">,</span> <span class="n">default</span><span class="p">,</span> <span class="n">namespaces</span><span class="p">)</span></span><a href="#l378"></a>
<span id="l379"></span><a href="#l379"></a>
<span id="l380">    <span class="c">##</span></span><a href="#l380"></a>
<span id="l381">    <span class="c"># Finds all matching subelements, by tag name or path.</span></span><a href="#l381"></a>
<span id="l382">    <span class="c">#</span></span><a href="#l382"></a>
<span id="l383">    <span class="c"># @param path What element to look for.</span></span><a href="#l383"></a>
<span id="l384">    <span class="c"># @keyparam namespaces Optional namespace prefix map.</span></span><a href="#l384"></a>
<span id="l385">    <span class="c"># @return A list or other sequence containing all matching elements,</span></span><a href="#l385"></a>
<span id="l386">    <span class="c">#    in document order.</span></span><a href="#l386"></a>
<span id="l387">    <span class="c"># @defreturn list of Element instances</span></span><a href="#l387"></a>
<span id="l388"></span><a href="#l388"></a>
<span id="l389">    <span class="k">def</span> <span class="nf">findall</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">,</span> <span class="n">namespaces</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l389"></a>
<span id="l390">        <span class="k">return</span> <span class="n">ElementPath</span><span class="o">.</span><span class="n">findall</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">,</span> <span class="n">namespaces</span><span class="p">)</span></span><a href="#l390"></a>
<span id="l391"></span><a href="#l391"></a>
<span id="l392">    <span class="c">##</span></span><a href="#l392"></a>
<span id="l393">    <span class="c"># Finds all matching subelements, by tag name or path.</span></span><a href="#l393"></a>
<span id="l394">    <span class="c">#</span></span><a href="#l394"></a>
<span id="l395">    <span class="c"># @param path What element to look for.</span></span><a href="#l395"></a>
<span id="l396">    <span class="c"># @keyparam namespaces Optional namespace prefix map.</span></span><a href="#l396"></a>
<span id="l397">    <span class="c"># @return An iterator or sequence containing all matching elements,</span></span><a href="#l397"></a>
<span id="l398">    <span class="c">#    in document order.</span></span><a href="#l398"></a>
<span id="l399">    <span class="c"># @defreturn a generated sequence of Element instances</span></span><a href="#l399"></a>
<span id="l400"></span><a href="#l400"></a>
<span id="l401">    <span class="k">def</span> <span class="nf">iterfind</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">,</span> <span class="n">namespaces</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l401"></a>
<span id="l402">        <span class="k">return</span> <span class="n">ElementPath</span><span class="o">.</span><span class="n">iterfind</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">,</span> <span class="n">namespaces</span><span class="p">)</span></span><a href="#l402"></a>
<span id="l403"></span><a href="#l403"></a>
<span id="l404">    <span class="c">##</span></span><a href="#l404"></a>
<span id="l405">    <span class="c"># Resets an element.  This function removes all subelements, clears</span></span><a href="#l405"></a>
<span id="l406">    <span class="c"># all attributes, and sets the &lt;b&gt;text&lt;/b&gt; and &lt;b&gt;tail&lt;/b&gt; attributes</span></span><a href="#l406"></a>
<span id="l407">    <span class="c"># to None.</span></span><a href="#l407"></a>
<span id="l408"></span><a href="#l408"></a>
<span id="l409">    <span class="k">def</span> <span class="nf">clear</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l409"></a>
<span id="l410">        <span class="bp">self</span><span class="o">.</span><span class="n">attrib</span><span class="o">.</span><span class="n">clear</span><span class="p">()</span></span><a href="#l410"></a>
<span id="l411">        <span class="bp">self</span><span class="o">.</span><span class="n">_children</span> <span class="o">=</span> <span class="p">[]</span></span><a href="#l411"></a>
<span id="l412">        <span class="bp">self</span><span class="o">.</span><span class="n">text</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tail</span> <span class="o">=</span> <span class="bp">None</span></span><a href="#l412"></a>
<span id="l413"></span><a href="#l413"></a>
<span id="l414">    <span class="c">##</span></span><a href="#l414"></a>
<span id="l415">    <span class="c"># Gets an element attribute.  Equivalent to &lt;b&gt;attrib.get&lt;/b&gt;, but</span></span><a href="#l415"></a>
<span id="l416">    <span class="c"># some implementations may handle this a bit more efficiently.</span></span><a href="#l416"></a>
<span id="l417">    <span class="c">#</span></span><a href="#l417"></a>
<span id="l418">    <span class="c"># @param key What attribute to look for.</span></span><a href="#l418"></a>
<span id="l419">    <span class="c"># @param default What to return if the attribute was not found.</span></span><a href="#l419"></a>
<span id="l420">    <span class="c"># @return The attribute value, or the default value, if the</span></span><a href="#l420"></a>
<span id="l421">    <span class="c">#     attribute was not found.</span></span><a href="#l421"></a>
<span id="l422">    <span class="c"># @defreturn string or None</span></span><a href="#l422"></a>
<span id="l423"></span><a href="#l423"></a>
<span id="l424">    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l424"></a>
<span id="l425">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">attrib</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">default</span><span class="p">)</span></span><a href="#l425"></a>
<span id="l426"></span><a href="#l426"></a>
<span id="l427">    <span class="c">##</span></span><a href="#l427"></a>
<span id="l428">    <span class="c"># Sets an element attribute.  Equivalent to &lt;b&gt;attrib[key] = value&lt;/b&gt;,</span></span><a href="#l428"></a>
<span id="l429">    <span class="c"># but some implementations may handle this a bit more efficiently.</span></span><a href="#l429"></a>
<span id="l430">    <span class="c">#</span></span><a href="#l430"></a>
<span id="l431">    <span class="c"># @param key What attribute to set.</span></span><a href="#l431"></a>
<span id="l432">    <span class="c"># @param value The attribute value.</span></span><a href="#l432"></a>
<span id="l433"></span><a href="#l433"></a>
<span id="l434">    <span class="k">def</span> <span class="nf">set</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span><span class="p">):</span></span><a href="#l434"></a>
<span id="l435">        <span class="bp">self</span><span class="o">.</span><span class="n">attrib</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="n">value</span></span><a href="#l435"></a>
<span id="l436"></span><a href="#l436"></a>
<span id="l437">    <span class="c">##</span></span><a href="#l437"></a>
<span id="l438">    <span class="c"># Gets a list of attribute names.  The names are returned in an</span></span><a href="#l438"></a>
<span id="l439">    <span class="c"># arbitrary order (just like for an ordinary Python dictionary).</span></span><a href="#l439"></a>
<span id="l440">    <span class="c"># Equivalent to &lt;b&gt;attrib.keys()&lt;/b&gt;.</span></span><a href="#l440"></a>
<span id="l441">    <span class="c">#</span></span><a href="#l441"></a>
<span id="l442">    <span class="c"># @return A list of element attribute names.</span></span><a href="#l442"></a>
<span id="l443">    <span class="c"># @defreturn list of strings</span></span><a href="#l443"></a>
<span id="l444"></span><a href="#l444"></a>
<span id="l445">    <span class="k">def</span> <span class="nf">keys</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l445"></a>
<span id="l446">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">attrib</span><span class="o">.</span><span class="n">keys</span><span class="p">()</span></span><a href="#l446"></a>
<span id="l447"></span><a href="#l447"></a>
<span id="l448">    <span class="c">##</span></span><a href="#l448"></a>
<span id="l449">    <span class="c"># Gets element attributes, as a sequence.  The attributes are</span></span><a href="#l449"></a>
<span id="l450">    <span class="c"># returned in an arbitrary order.  Equivalent to &lt;b&gt;attrib.items()&lt;/b&gt;.</span></span><a href="#l450"></a>
<span id="l451">    <span class="c">#</span></span><a href="#l451"></a>
<span id="l452">    <span class="c"># @return A list of (name, value) tuples for all attributes.</span></span><a href="#l452"></a>
<span id="l453">    <span class="c"># @defreturn list of (string, string) tuples</span></span><a href="#l453"></a>
<span id="l454"></span><a href="#l454"></a>
<span id="l455">    <span class="k">def</span> <span class="nf">items</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l455"></a>
<span id="l456">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">attrib</span><span class="o">.</span><span class="n">items</span><span class="p">()</span></span><a href="#l456"></a>
<span id="l457"></span><a href="#l457"></a>
<span id="l458">    <span class="c">##</span></span><a href="#l458"></a>
<span id="l459">    <span class="c"># Creates a tree iterator.  The iterator loops over this element</span></span><a href="#l459"></a>
<span id="l460">    <span class="c"># and all subelements, in document order, and returns all elements</span></span><a href="#l460"></a>
<span id="l461">    <span class="c"># with a matching tag.</span></span><a href="#l461"></a>
<span id="l462">    <span class="c"># &lt;p&gt;</span></span><a href="#l462"></a>
<span id="l463">    <span class="c"># If the tree structure is modified during iteration, new or removed</span></span><a href="#l463"></a>
<span id="l464">    <span class="c"># elements may or may not be included.  To get a stable set, use the</span></span><a href="#l464"></a>
<span id="l465">    <span class="c"># list() function on the iterator, and loop over the resulting list.</span></span><a href="#l465"></a>
<span id="l466">    <span class="c">#</span></span><a href="#l466"></a>
<span id="l467">    <span class="c"># @param tag What tags to look for (default is to return all elements).</span></span><a href="#l467"></a>
<span id="l468">    <span class="c"># @return An iterator containing all the matching elements.</span></span><a href="#l468"></a>
<span id="l469">    <span class="c"># @defreturn iterator</span></span><a href="#l469"></a>
<span id="l470"></span><a href="#l470"></a>
<span id="l471">    <span class="k">def</span> <span class="nf">iter</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tag</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l471"></a>
<span id="l472">        <span class="k">if</span> <span class="n">tag</span> <span class="o">==</span> <span class="s">&quot;*&quot;</span><span class="p">:</span></span><a href="#l472"></a>
<span id="l473">            <span class="n">tag</span> <span class="o">=</span> <span class="bp">None</span></span><a href="#l473"></a>
<span id="l474">        <span class="k">if</span> <span class="n">tag</span> <span class="ow">is</span> <span class="bp">None</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">tag</span> <span class="o">==</span> <span class="n">tag</span><span class="p">:</span></span><a href="#l474"></a>
<span id="l475">            <span class="k">yield</span> <span class="bp">self</span></span><a href="#l475"></a>
<span id="l476">        <span class="k">for</span> <span class="n">e</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_children</span><span class="p">:</span></span><a href="#l476"></a>
<span id="l477">            <span class="k">for</span> <span class="n">e</span> <span class="ow">in</span> <span class="n">e</span><span class="o">.</span><span class="n">iter</span><span class="p">(</span><span class="n">tag</span><span class="p">):</span></span><a href="#l477"></a>
<span id="l478">                <span class="k">yield</span> <span class="n">e</span></span><a href="#l478"></a>
<span id="l479"></span><a href="#l479"></a>
<span id="l480">    <span class="c"># compatibility</span></span><a href="#l480"></a>
<span id="l481">    <span class="k">def</span> <span class="nf">getiterator</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tag</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l481"></a>
<span id="l482">        <span class="c"># Change for a DeprecationWarning in 1.4</span></span><a href="#l482"></a>
<span id="l483">        <span class="n">warnings</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span></span><a href="#l483"></a>
<span id="l484">            <span class="s">&quot;This method will be removed in future versions.  &quot;</span></span><a href="#l484"></a>
<span id="l485">            <span class="s">&quot;Use &#39;elem.iter()&#39; or &#39;list(elem.iter())&#39; instead.&quot;</span><span class="p">,</span></span><a href="#l485"></a>
<span id="l486">            <span class="ne">PendingDeprecationWarning</span><span class="p">,</span> <span class="n">stacklevel</span><span class="o">=</span><span class="mi">2</span></span><a href="#l486"></a>
<span id="l487">        <span class="p">)</span></span><a href="#l487"></a>
<span id="l488">        <span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">iter</span><span class="p">(</span><span class="n">tag</span><span class="p">))</span></span><a href="#l488"></a>
<span id="l489"></span><a href="#l489"></a>
<span id="l490">    <span class="c">##</span></span><a href="#l490"></a>
<span id="l491">    <span class="c"># Creates a text iterator.  The iterator loops over this element</span></span><a href="#l491"></a>
<span id="l492">    <span class="c"># and all subelements, in document order, and returns all inner</span></span><a href="#l492"></a>
<span id="l493">    <span class="c"># text.</span></span><a href="#l493"></a>
<span id="l494">    <span class="c">#</span></span><a href="#l494"></a>
<span id="l495">    <span class="c"># @return An iterator containing all inner text.</span></span><a href="#l495"></a>
<span id="l496">    <span class="c"># @defreturn iterator</span></span><a href="#l496"></a>
<span id="l497"></span><a href="#l497"></a>
<span id="l498">    <span class="k">def</span> <span class="nf">itertext</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l498"></a>
<span id="l499">        <span class="n">tag</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tag</span></span><a href="#l499"></a>
<span id="l500">        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">tag</span><span class="p">,</span> <span class="nb">basestring</span><span class="p">)</span> <span class="ow">and</span> <span class="n">tag</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l500"></a>
<span id="l501">            <span class="k">return</span></span><a href="#l501"></a>
<span id="l502">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">text</span><span class="p">:</span></span><a href="#l502"></a>
<span id="l503">            <span class="k">yield</span> <span class="bp">self</span><span class="o">.</span><span class="n">text</span></span><a href="#l503"></a>
<span id="l504">        <span class="k">for</span> <span class="n">e</span> <span class="ow">in</span> <span class="bp">self</span><span class="p">:</span></span><a href="#l504"></a>
<span id="l505">            <span class="k">for</span> <span class="n">s</span> <span class="ow">in</span> <span class="n">e</span><span class="o">.</span><span class="n">itertext</span><span class="p">():</span></span><a href="#l505"></a>
<span id="l506">                <span class="k">yield</span> <span class="n">s</span></span><a href="#l506"></a>
<span id="l507">            <span class="k">if</span> <span class="n">e</span><span class="o">.</span><span class="n">tail</span><span class="p">:</span></span><a href="#l507"></a>
<span id="l508">                <span class="k">yield</span> <span class="n">e</span><span class="o">.</span><span class="n">tail</span></span><a href="#l508"></a>
<span id="l509"></span><a href="#l509"></a>
<span id="l510"><span class="c"># compatibility</span></span><a href="#l510"></a>
<span id="l511"><span class="n">_Element</span> <span class="o">=</span> <span class="n">_ElementInterface</span> <span class="o">=</span> <span class="n">Element</span></span><a href="#l511"></a>
<span id="l512"></span><a href="#l512"></a>
<span id="l513"><span class="c">##</span></span><a href="#l513"></a>
<span id="l514"><span class="c"># Subelement factory.  This function creates an element instance, and</span></span><a href="#l514"></a>
<span id="l515"><span class="c"># appends it to an existing element.</span></span><a href="#l515"></a>
<span id="l516"><span class="c"># &lt;p&gt;</span></span><a href="#l516"></a>
<span id="l517"><span class="c"># The element name, attribute names, and attribute values can be</span></span><a href="#l517"></a>
<span id="l518"><span class="c"># either 8-bit ASCII strings or Unicode strings.</span></span><a href="#l518"></a>
<span id="l519"><span class="c">#</span></span><a href="#l519"></a>
<span id="l520"><span class="c"># @param parent The parent element.</span></span><a href="#l520"></a>
<span id="l521"><span class="c"># @param tag The subelement name.</span></span><a href="#l521"></a>
<span id="l522"><span class="c"># @param attrib An optional dictionary, containing element attributes.</span></span><a href="#l522"></a>
<span id="l523"><span class="c"># @param **extra Additional attributes, given as keyword arguments.</span></span><a href="#l523"></a>
<span id="l524"><span class="c"># @return An element instance.</span></span><a href="#l524"></a>
<span id="l525"><span class="c"># @defreturn Element</span></span><a href="#l525"></a>
<span id="l526"></span><a href="#l526"></a>
<span id="l527"><span class="k">def</span> <span class="nf">SubElement</span><span class="p">(</span><span class="n">parent</span><span class="p">,</span> <span class="n">tag</span><span class="p">,</span> <span class="n">attrib</span><span class="o">=</span><span class="p">{},</span> <span class="o">**</span><span class="n">extra</span><span class="p">):</span></span><a href="#l527"></a>
<span id="l528">    <span class="n">attrib</span> <span class="o">=</span> <span class="n">attrib</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span></span><a href="#l528"></a>
<span id="l529">    <span class="n">attrib</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">extra</span><span class="p">)</span></span><a href="#l529"></a>
<span id="l530">    <span class="n">element</span> <span class="o">=</span> <span class="n">parent</span><span class="o">.</span><span class="n">makeelement</span><span class="p">(</span><span class="n">tag</span><span class="p">,</span> <span class="n">attrib</span><span class="p">)</span></span><a href="#l530"></a>
<span id="l531">    <span class="n">parent</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">element</span><span class="p">)</span></span><a href="#l531"></a>
<span id="l532">    <span class="k">return</span> <span class="n">element</span></span><a href="#l532"></a>
<span id="l533"></span><a href="#l533"></a>
<span id="l534"><span class="c">##</span></span><a href="#l534"></a>
<span id="l535"><span class="c"># Comment element factory.  This factory function creates a special</span></span><a href="#l535"></a>
<span id="l536"><span class="c"># element that will be serialized as an XML comment by the standard</span></span><a href="#l536"></a>
<span id="l537"><span class="c"># serializer.</span></span><a href="#l537"></a>
<span id="l538"><span class="c"># &lt;p&gt;</span></span><a href="#l538"></a>
<span id="l539"><span class="c"># The comment string can be either an 8-bit ASCII string or a Unicode</span></span><a href="#l539"></a>
<span id="l540"><span class="c"># string.</span></span><a href="#l540"></a>
<span id="l541"><span class="c">#</span></span><a href="#l541"></a>
<span id="l542"><span class="c"># @param text A string containing the comment string.</span></span><a href="#l542"></a>
<span id="l543"><span class="c"># @return An element instance, representing a comment.</span></span><a href="#l543"></a>
<span id="l544"><span class="c"># @defreturn Element</span></span><a href="#l544"></a>
<span id="l545"></span><a href="#l545"></a>
<span id="l546"><span class="k">def</span> <span class="nf">Comment</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l546"></a>
<span id="l547">    <span class="n">element</span> <span class="o">=</span> <span class="n">Element</span><span class="p">(</span><span class="n">Comment</span><span class="p">)</span></span><a href="#l547"></a>
<span id="l548">    <span class="n">element</span><span class="o">.</span><span class="n">text</span> <span class="o">=</span> <span class="n">text</span></span><a href="#l548"></a>
<span id="l549">    <span class="k">return</span> <span class="n">element</span></span><a href="#l549"></a>
<span id="l550"></span><a href="#l550"></a>
<span id="l551"><span class="c">##</span></span><a href="#l551"></a>
<span id="l552"><span class="c"># PI element factory.  This factory function creates a special element</span></span><a href="#l552"></a>
<span id="l553"><span class="c"># that will be serialized as an XML processing instruction by the standard</span></span><a href="#l553"></a>
<span id="l554"><span class="c"># serializer.</span></span><a href="#l554"></a>
<span id="l555"><span class="c">#</span></span><a href="#l555"></a>
<span id="l556"><span class="c"># @param target A string containing the PI target.</span></span><a href="#l556"></a>
<span id="l557"><span class="c"># @param text A string containing the PI contents, if any.</span></span><a href="#l557"></a>
<span id="l558"><span class="c"># @return An element instance, representing a PI.</span></span><a href="#l558"></a>
<span id="l559"><span class="c"># @defreturn Element</span></span><a href="#l559"></a>
<span id="l560"></span><a href="#l560"></a>
<span id="l561"><span class="k">def</span> <span class="nf">ProcessingInstruction</span><span class="p">(</span><span class="n">target</span><span class="p">,</span> <span class="n">text</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l561"></a>
<span id="l562">    <span class="n">element</span> <span class="o">=</span> <span class="n">Element</span><span class="p">(</span><span class="n">ProcessingInstruction</span><span class="p">)</span></span><a href="#l562"></a>
<span id="l563">    <span class="n">element</span><span class="o">.</span><span class="n">text</span> <span class="o">=</span> <span class="n">target</span></span><a href="#l563"></a>
<span id="l564">    <span class="k">if</span> <span class="n">text</span><span class="p">:</span></span><a href="#l564"></a>
<span id="l565">        <span class="n">element</span><span class="o">.</span><span class="n">text</span> <span class="o">=</span> <span class="n">element</span><span class="o">.</span><span class="n">text</span> <span class="o">+</span> <span class="s">&quot; &quot;</span> <span class="o">+</span> <span class="n">text</span></span><a href="#l565"></a>
<span id="l566">    <span class="k">return</span> <span class="n">element</span></span><a href="#l566"></a>
<span id="l567"></span><a href="#l567"></a>
<span id="l568"><span class="n">PI</span> <span class="o">=</span> <span class="n">ProcessingInstruction</span></span><a href="#l568"></a>
<span id="l569"></span><a href="#l569"></a>
<span id="l570"><span class="c">##</span></span><a href="#l570"></a>
<span id="l571"><span class="c"># QName wrapper.  This can be used to wrap a QName attribute value, in</span></span><a href="#l571"></a>
<span id="l572"><span class="c"># order to get proper namespace handling on output.</span></span><a href="#l572"></a>
<span id="l573"><span class="c">#</span></span><a href="#l573"></a>
<span id="l574"><span class="c"># @param text A string containing the QName value, in the form {uri}local,</span></span><a href="#l574"></a>
<span id="l575"><span class="c">#     or, if the tag argument is given, the URI part of a QName.</span></span><a href="#l575"></a>
<span id="l576"><span class="c"># @param tag Optional tag.  If given, the first argument is interpreted as</span></span><a href="#l576"></a>
<span id="l577"><span class="c">#     an URI, and this argument is interpreted as a local name.</span></span><a href="#l577"></a>
<span id="l578"><span class="c"># @return An opaque object, representing the QName.</span></span><a href="#l578"></a>
<span id="l579"></span><a href="#l579"></a>
<span id="l580"><span class="k">class</span> <span class="nc">QName</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></span><a href="#l580"></a>
<span id="l581">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text_or_uri</span><span class="p">,</span> <span class="n">tag</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l581"></a>
<span id="l582">        <span class="k">if</span> <span class="n">tag</span><span class="p">:</span></span><a href="#l582"></a>
<span id="l583">            <span class="n">text_or_uri</span> <span class="o">=</span> <span class="s">&quot;{</span><span class="si">%s</span><span class="s">}</span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">text_or_uri</span><span class="p">,</span> <span class="n">tag</span><span class="p">)</span></span><a href="#l583"></a>
<span id="l584">        <span class="bp">self</span><span class="o">.</span><span class="n">text</span> <span class="o">=</span> <span class="n">text_or_uri</span></span><a href="#l584"></a>
<span id="l585">    <span class="k">def</span> <span class="nf">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l585"></a>
<span id="l586">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">text</span></span><a href="#l586"></a>
<span id="l587">    <span class="k">def</span> <span class="nf">__hash__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l587"></a>
<span id="l588">        <span class="k">return</span> <span class="nb">hash</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">text</span><span class="p">)</span></span><a href="#l588"></a>
<span id="l589">    <span class="k">def</span> <span class="nf">__cmp__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span></span><a href="#l589"></a>
<span id="l590">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">QName</span><span class="p">):</span></span><a href="#l590"></a>
<span id="l591">            <span class="k">return</span> <span class="nb">cmp</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">text</span><span class="p">,</span> <span class="n">other</span><span class="o">.</span><span class="n">text</span><span class="p">)</span></span><a href="#l591"></a>
<span id="l592">        <span class="k">return</span> <span class="nb">cmp</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">text</span><span class="p">,</span> <span class="n">other</span><span class="p">)</span></span><a href="#l592"></a>
<span id="l593"></span><a href="#l593"></a>
<span id="l594"><span class="c"># --------------------------------------------------------------------</span></span><a href="#l594"></a>
<span id="l595"></span><a href="#l595"></a>
<span id="l596"><span class="c">##</span></span><a href="#l596"></a>
<span id="l597"><span class="c"># ElementTree wrapper class.  This class represents an entire element</span></span><a href="#l597"></a>
<span id="l598"><span class="c"># hierarchy, and adds some extra support for serialization to and from</span></span><a href="#l598"></a>
<span id="l599"><span class="c"># standard XML.</span></span><a href="#l599"></a>
<span id="l600"><span class="c">#</span></span><a href="#l600"></a>
<span id="l601"><span class="c"># @param element Optional root element.</span></span><a href="#l601"></a>
<span id="l602"><span class="c"># @keyparam file Optional file handle or file name.  If given, the</span></span><a href="#l602"></a>
<span id="l603"><span class="c">#     tree is initialized with the contents of this XML file.</span></span><a href="#l603"></a>
<span id="l604"></span><a href="#l604"></a>
<span id="l605"><span class="k">class</span> <span class="nc">ElementTree</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></span><a href="#l605"></a>
<span id="l606"></span><a href="#l606"></a>
<span id="l607">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">element</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="nb">file</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l607"></a>
<span id="l608">        <span class="c"># assert element is None or iselement(element)</span></span><a href="#l608"></a>
<span id="l609">        <span class="bp">self</span><span class="o">.</span><span class="n">_root</span> <span class="o">=</span> <span class="n">element</span> <span class="c"># first node</span></span><a href="#l609"></a>
<span id="l610">        <span class="k">if</span> <span class="nb">file</span><span class="p">:</span></span><a href="#l610"></a>
<span id="l611">            <span class="bp">self</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="nb">file</span><span class="p">)</span></span><a href="#l611"></a>
<span id="l612"></span><a href="#l612"></a>
<span id="l613">    <span class="c">##</span></span><a href="#l613"></a>
<span id="l614">    <span class="c"># Gets the root element for this tree.</span></span><a href="#l614"></a>
<span id="l615">    <span class="c">#</span></span><a href="#l615"></a>
<span id="l616">    <span class="c"># @return An element instance.</span></span><a href="#l616"></a>
<span id="l617">    <span class="c"># @defreturn Element</span></span><a href="#l617"></a>
<span id="l618"></span><a href="#l618"></a>
<span id="l619">    <span class="k">def</span> <span class="nf">getroot</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l619"></a>
<span id="l620">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_root</span></span><a href="#l620"></a>
<span id="l621"></span><a href="#l621"></a>
<span id="l622">    <span class="c">##</span></span><a href="#l622"></a>
<span id="l623">    <span class="c"># Replaces the root element for this tree.  This discards the</span></span><a href="#l623"></a>
<span id="l624">    <span class="c"># current contents of the tree, and replaces it with the given</span></span><a href="#l624"></a>
<span id="l625">    <span class="c"># element.  Use with care.</span></span><a href="#l625"></a>
<span id="l626">    <span class="c">#</span></span><a href="#l626"></a>
<span id="l627">    <span class="c"># @param element An element instance.</span></span><a href="#l627"></a>
<span id="l628"></span><a href="#l628"></a>
<span id="l629">    <span class="k">def</span> <span class="nf">_setroot</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">element</span><span class="p">):</span></span><a href="#l629"></a>
<span id="l630">        <span class="c"># assert iselement(element)</span></span><a href="#l630"></a>
<span id="l631">        <span class="bp">self</span><span class="o">.</span><span class="n">_root</span> <span class="o">=</span> <span class="n">element</span></span><a href="#l631"></a>
<span id="l632"></span><a href="#l632"></a>
<span id="l633">    <span class="c">##</span></span><a href="#l633"></a>
<span id="l634">    <span class="c"># Loads an external XML document into this element tree.</span></span><a href="#l634"></a>
<span id="l635">    <span class="c">#</span></span><a href="#l635"></a>
<span id="l636">    <span class="c"># @param source A file name or file object.  If a file object is</span></span><a href="#l636"></a>
<span id="l637">    <span class="c">#     given, it only has to implement a &lt;b&gt;read(n)&lt;/b&gt; method.</span></span><a href="#l637"></a>
<span id="l638">    <span class="c"># @keyparam parser An optional parser instance.  If not given, the</span></span><a href="#l638"></a>
<span id="l639">    <span class="c">#     standard {@link XMLParser} parser is used.</span></span><a href="#l639"></a>
<span id="l640">    <span class="c"># @return The document root element.</span></span><a href="#l640"></a>
<span id="l641">    <span class="c"># @defreturn Element</span></span><a href="#l641"></a>
<span id="l642">    <span class="c"># @exception ParseError If the parser fails to parse the document.</span></span><a href="#l642"></a>
<span id="l643"></span><a href="#l643"></a>
<span id="l644">    <span class="k">def</span> <span class="nf">parse</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">source</span><span class="p">,</span> <span class="n">parser</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l644"></a>
<span id="l645">        <span class="n">close_source</span> <span class="o">=</span> <span class="bp">False</span></span><a href="#l645"></a>
<span id="l646">        <span class="k">if</span> <span class="ow">not</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">source</span><span class="p">,</span> <span class="s">&quot;read&quot;</span><span class="p">):</span></span><a href="#l646"></a>
<span id="l647">            <span class="n">source</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">source</span><span class="p">,</span> <span class="s">&quot;rb&quot;</span><span class="p">)</span></span><a href="#l647"></a>
<span id="l648">            <span class="n">close_source</span> <span class="o">=</span> <span class="bp">True</span></span><a href="#l648"></a>
<span id="l649">        <span class="k">try</span><span class="p">:</span></span><a href="#l649"></a>
<span id="l650">            <span class="k">if</span> <span class="ow">not</span> <span class="n">parser</span><span class="p">:</span></span><a href="#l650"></a>
<span id="l651">                <span class="n">parser</span> <span class="o">=</span> <span class="n">XMLParser</span><span class="p">(</span><span class="n">target</span><span class="o">=</span><span class="n">TreeBuilder</span><span class="p">())</span></span><a href="#l651"></a>
<span id="l652">            <span class="k">while</span> <span class="mi">1</span><span class="p">:</span></span><a href="#l652"></a>
<span id="l653">                <span class="n">data</span> <span class="o">=</span> <span class="n">source</span><span class="o">.</span><span class="n">read</span><span class="p">(</span><span class="mi">65536</span><span class="p">)</span></span><a href="#l653"></a>
<span id="l654">                <span class="k">if</span> <span class="ow">not</span> <span class="n">data</span><span class="p">:</span></span><a href="#l654"></a>
<span id="l655">                    <span class="k">break</span></span><a href="#l655"></a>
<span id="l656">                <span class="n">parser</span><span class="o">.</span><span class="n">feed</span><span class="p">(</span><span class="n">data</span><span class="p">)</span></span><a href="#l656"></a>
<span id="l657">            <span class="bp">self</span><span class="o">.</span><span class="n">_root</span> <span class="o">=</span> <span class="n">parser</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></span><a href="#l657"></a>
<span id="l658">            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_root</span></span><a href="#l658"></a>
<span id="l659">        <span class="k">finally</span><span class="p">:</span></span><a href="#l659"></a>
<span id="l660">            <span class="k">if</span> <span class="n">close_source</span><span class="p">:</span></span><a href="#l660"></a>
<span id="l661">                <span class="n">source</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></span><a href="#l661"></a>
<span id="l662"></span><a href="#l662"></a>
<span id="l663">    <span class="c">##</span></span><a href="#l663"></a>
<span id="l664">    <span class="c"># Creates a tree iterator for the root element.  The iterator loops</span></span><a href="#l664"></a>
<span id="l665">    <span class="c"># over all elements in this tree, in document order.</span></span><a href="#l665"></a>
<span id="l666">    <span class="c">#</span></span><a href="#l666"></a>
<span id="l667">    <span class="c"># @param tag What tags to look for (default is to return all elements)</span></span><a href="#l667"></a>
<span id="l668">    <span class="c"># @return An iterator.</span></span><a href="#l668"></a>
<span id="l669">    <span class="c"># @defreturn iterator</span></span><a href="#l669"></a>
<span id="l670"></span><a href="#l670"></a>
<span id="l671">    <span class="k">def</span> <span class="nf">iter</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tag</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l671"></a>
<span id="l672">        <span class="c"># assert self._root is not None</span></span><a href="#l672"></a>
<span id="l673">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_root</span><span class="o">.</span><span class="n">iter</span><span class="p">(</span><span class="n">tag</span><span class="p">)</span></span><a href="#l673"></a>
<span id="l674"></span><a href="#l674"></a>
<span id="l675">    <span class="c"># compatibility</span></span><a href="#l675"></a>
<span id="l676">    <span class="k">def</span> <span class="nf">getiterator</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tag</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l676"></a>
<span id="l677">        <span class="c"># Change for a DeprecationWarning in 1.4</span></span><a href="#l677"></a>
<span id="l678">        <span class="n">warnings</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span></span><a href="#l678"></a>
<span id="l679">            <span class="s">&quot;This method will be removed in future versions.  &quot;</span></span><a href="#l679"></a>
<span id="l680">            <span class="s">&quot;Use &#39;tree.iter()&#39; or &#39;list(tree.iter())&#39; instead.&quot;</span><span class="p">,</span></span><a href="#l680"></a>
<span id="l681">            <span class="ne">PendingDeprecationWarning</span><span class="p">,</span> <span class="n">stacklevel</span><span class="o">=</span><span class="mi">2</span></span><a href="#l681"></a>
<span id="l682">        <span class="p">)</span></span><a href="#l682"></a>
<span id="l683">        <span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">iter</span><span class="p">(</span><span class="n">tag</span><span class="p">))</span></span><a href="#l683"></a>
<span id="l684"></span><a href="#l684"></a>
<span id="l685">    <span class="c">##</span></span><a href="#l685"></a>
<span id="l686">    <span class="c"># Same as getroot().find(path), starting at the root of the</span></span><a href="#l686"></a>
<span id="l687">    <span class="c"># tree.</span></span><a href="#l687"></a>
<span id="l688">    <span class="c">#</span></span><a href="#l688"></a>
<span id="l689">    <span class="c"># @param path What element to look for.</span></span><a href="#l689"></a>
<span id="l690">    <span class="c"># @keyparam namespaces Optional namespace prefix map.</span></span><a href="#l690"></a>
<span id="l691">    <span class="c"># @return The first matching element, or None if no element was found.</span></span><a href="#l691"></a>
<span id="l692">    <span class="c"># @defreturn Element or None</span></span><a href="#l692"></a>
<span id="l693"></span><a href="#l693"></a>
<span id="l694">    <span class="k">def</span> <span class="nf">find</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">,</span> <span class="n">namespaces</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l694"></a>
<span id="l695">        <span class="c"># assert self._root is not None</span></span><a href="#l695"></a>
<span id="l696">        <span class="k">if</span> <span class="n">path</span><span class="p">[:</span><span class="mi">1</span><span class="p">]</span> <span class="o">==</span> <span class="s">&quot;/&quot;</span><span class="p">:</span></span><a href="#l696"></a>
<span id="l697">            <span class="n">path</span> <span class="o">=</span> <span class="s">&quot;.&quot;</span> <span class="o">+</span> <span class="n">path</span></span><a href="#l697"></a>
<span id="l698">            <span class="n">warnings</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span></span><a href="#l698"></a>
<span id="l699">                <span class="s">&quot;This search is broken in 1.3 and earlier, and will be &quot;</span></span><a href="#l699"></a>
<span id="l700">                <span class="s">&quot;fixed in a future version.  If you rely on the current &quot;</span></span><a href="#l700"></a>
<span id="l701">                <span class="s">&quot;behaviour, change it to </span><span class="si">%r</span><span class="s">&quot;</span> <span class="o">%</span> <span class="n">path</span><span class="p">,</span></span><a href="#l701"></a>
<span id="l702">                <span class="ne">FutureWarning</span><span class="p">,</span> <span class="n">stacklevel</span><span class="o">=</span><span class="mi">2</span></span><a href="#l702"></a>
<span id="l703">                <span class="p">)</span></span><a href="#l703"></a>
<span id="l704">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_root</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="n">path</span><span class="p">,</span> <span class="n">namespaces</span><span class="p">)</span></span><a href="#l704"></a>
<span id="l705"></span><a href="#l705"></a>
<span id="l706">    <span class="c">##</span></span><a href="#l706"></a>
<span id="l707">    <span class="c"># Same as getroot().findtext(path), starting at the root of the tree.</span></span><a href="#l707"></a>
<span id="l708">    <span class="c">#</span></span><a href="#l708"></a>
<span id="l709">    <span class="c"># @param path What element to look for.</span></span><a href="#l709"></a>
<span id="l710">    <span class="c"># @param default What to return if the element was not found.</span></span><a href="#l710"></a>
<span id="l711">    <span class="c"># @keyparam namespaces Optional namespace prefix map.</span></span><a href="#l711"></a>
<span id="l712">    <span class="c"># @return The text content of the first matching element, or the</span></span><a href="#l712"></a>
<span id="l713">    <span class="c">#     default value no element was found.  Note that if the element</span></span><a href="#l713"></a>
<span id="l714">    <span class="c">#     is found, but has no text content, this method returns an</span></span><a href="#l714"></a>
<span id="l715">    <span class="c">#     empty string.</span></span><a href="#l715"></a>
<span id="l716">    <span class="c"># @defreturn string</span></span><a href="#l716"></a>
<span id="l717"></span><a href="#l717"></a>
<span id="l718">    <span class="k">def</span> <span class="nf">findtext</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">namespaces</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l718"></a>
<span id="l719">        <span class="c"># assert self._root is not None</span></span><a href="#l719"></a>
<span id="l720">        <span class="k">if</span> <span class="n">path</span><span class="p">[:</span><span class="mi">1</span><span class="p">]</span> <span class="o">==</span> <span class="s">&quot;/&quot;</span><span class="p">:</span></span><a href="#l720"></a>
<span id="l721">            <span class="n">path</span> <span class="o">=</span> <span class="s">&quot;.&quot;</span> <span class="o">+</span> <span class="n">path</span></span><a href="#l721"></a>
<span id="l722">            <span class="n">warnings</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span></span><a href="#l722"></a>
<span id="l723">                <span class="s">&quot;This search is broken in 1.3 and earlier, and will be &quot;</span></span><a href="#l723"></a>
<span id="l724">                <span class="s">&quot;fixed in a future version.  If you rely on the current &quot;</span></span><a href="#l724"></a>
<span id="l725">                <span class="s">&quot;behaviour, change it to </span><span class="si">%r</span><span class="s">&quot;</span> <span class="o">%</span> <span class="n">path</span><span class="p">,</span></span><a href="#l725"></a>
<span id="l726">                <span class="ne">FutureWarning</span><span class="p">,</span> <span class="n">stacklevel</span><span class="o">=</span><span class="mi">2</span></span><a href="#l726"></a>
<span id="l727">                <span class="p">)</span></span><a href="#l727"></a>
<span id="l728">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_root</span><span class="o">.</span><span class="n">findtext</span><span class="p">(</span><span class="n">path</span><span class="p">,</span> <span class="n">default</span><span class="p">,</span> <span class="n">namespaces</span><span class="p">)</span></span><a href="#l728"></a>
<span id="l729"></span><a href="#l729"></a>
<span id="l730">    <span class="c">##</span></span><a href="#l730"></a>
<span id="l731">    <span class="c"># Same as getroot().findall(path), starting at the root of the tree.</span></span><a href="#l731"></a>
<span id="l732">    <span class="c">#</span></span><a href="#l732"></a>
<span id="l733">    <span class="c"># @param path What element to look for.</span></span><a href="#l733"></a>
<span id="l734">    <span class="c"># @keyparam namespaces Optional namespace prefix map.</span></span><a href="#l734"></a>
<span id="l735">    <span class="c"># @return A list or iterator containing all matching elements,</span></span><a href="#l735"></a>
<span id="l736">    <span class="c">#    in document order.</span></span><a href="#l736"></a>
<span id="l737">    <span class="c"># @defreturn list of Element instances</span></span><a href="#l737"></a>
<span id="l738"></span><a href="#l738"></a>
<span id="l739">    <span class="k">def</span> <span class="nf">findall</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">,</span> <span class="n">namespaces</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l739"></a>
<span id="l740">        <span class="c"># assert self._root is not None</span></span><a href="#l740"></a>
<span id="l741">        <span class="k">if</span> <span class="n">path</span><span class="p">[:</span><span class="mi">1</span><span class="p">]</span> <span class="o">==</span> <span class="s">&quot;/&quot;</span><span class="p">:</span></span><a href="#l741"></a>
<span id="l742">            <span class="n">path</span> <span class="o">=</span> <span class="s">&quot;.&quot;</span> <span class="o">+</span> <span class="n">path</span></span><a href="#l742"></a>
<span id="l743">            <span class="n">warnings</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span></span><a href="#l743"></a>
<span id="l744">                <span class="s">&quot;This search is broken in 1.3 and earlier, and will be &quot;</span></span><a href="#l744"></a>
<span id="l745">                <span class="s">&quot;fixed in a future version.  If you rely on the current &quot;</span></span><a href="#l745"></a>
<span id="l746">                <span class="s">&quot;behaviour, change it to </span><span class="si">%r</span><span class="s">&quot;</span> <span class="o">%</span> <span class="n">path</span><span class="p">,</span></span><a href="#l746"></a>
<span id="l747">                <span class="ne">FutureWarning</span><span class="p">,</span> <span class="n">stacklevel</span><span class="o">=</span><span class="mi">2</span></span><a href="#l747"></a>
<span id="l748">                <span class="p">)</span></span><a href="#l748"></a>
<span id="l749">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_root</span><span class="o">.</span><span class="n">findall</span><span class="p">(</span><span class="n">path</span><span class="p">,</span> <span class="n">namespaces</span><span class="p">)</span></span><a href="#l749"></a>
<span id="l750"></span><a href="#l750"></a>
<span id="l751">    <span class="c">##</span></span><a href="#l751"></a>
<span id="l752">    <span class="c"># Finds all matching subelements, by tag name or path.</span></span><a href="#l752"></a>
<span id="l753">    <span class="c"># Same as getroot().iterfind(path).</span></span><a href="#l753"></a>
<span id="l754">    <span class="c">#</span></span><a href="#l754"></a>
<span id="l755">    <span class="c"># @param path What element to look for.</span></span><a href="#l755"></a>
<span id="l756">    <span class="c"># @keyparam namespaces Optional namespace prefix map.</span></span><a href="#l756"></a>
<span id="l757">    <span class="c"># @return An iterator or sequence containing all matching elements,</span></span><a href="#l757"></a>
<span id="l758">    <span class="c">#    in document order.</span></span><a href="#l758"></a>
<span id="l759">    <span class="c"># @defreturn a generated sequence of Element instances</span></span><a href="#l759"></a>
<span id="l760"></span><a href="#l760"></a>
<span id="l761">    <span class="k">def</span> <span class="nf">iterfind</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">,</span> <span class="n">namespaces</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l761"></a>
<span id="l762">        <span class="c"># assert self._root is not None</span></span><a href="#l762"></a>
<span id="l763">        <span class="k">if</span> <span class="n">path</span><span class="p">[:</span><span class="mi">1</span><span class="p">]</span> <span class="o">==</span> <span class="s">&quot;/&quot;</span><span class="p">:</span></span><a href="#l763"></a>
<span id="l764">            <span class="n">path</span> <span class="o">=</span> <span class="s">&quot;.&quot;</span> <span class="o">+</span> <span class="n">path</span></span><a href="#l764"></a>
<span id="l765">            <span class="n">warnings</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span></span><a href="#l765"></a>
<span id="l766">                <span class="s">&quot;This search is broken in 1.3 and earlier, and will be &quot;</span></span><a href="#l766"></a>
<span id="l767">                <span class="s">&quot;fixed in a future version.  If you rely on the current &quot;</span></span><a href="#l767"></a>
<span id="l768">                <span class="s">&quot;behaviour, change it to </span><span class="si">%r</span><span class="s">&quot;</span> <span class="o">%</span> <span class="n">path</span><span class="p">,</span></span><a href="#l768"></a>
<span id="l769">                <span class="ne">FutureWarning</span><span class="p">,</span> <span class="n">stacklevel</span><span class="o">=</span><span class="mi">2</span></span><a href="#l769"></a>
<span id="l770">                <span class="p">)</span></span><a href="#l770"></a>
<span id="l771">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_root</span><span class="o">.</span><span class="n">iterfind</span><span class="p">(</span><span class="n">path</span><span class="p">,</span> <span class="n">namespaces</span><span class="p">)</span></span><a href="#l771"></a>
<span id="l772"></span><a href="#l772"></a>
<span id="l773">    <span class="c">##</span></span><a href="#l773"></a>
<span id="l774">    <span class="c"># Writes the element tree to a file, as XML.</span></span><a href="#l774"></a>
<span id="l775">    <span class="c">#</span></span><a href="#l775"></a>
<span id="l776">    <span class="c"># @def write(file, **options)</span></span><a href="#l776"></a>
<span id="l777">    <span class="c"># @param file A file name, or a file object opened for writing.</span></span><a href="#l777"></a>
<span id="l778">    <span class="c"># @param **options Options, given as keyword arguments.</span></span><a href="#l778"></a>
<span id="l779">    <span class="c"># @keyparam encoding Optional output encoding (default is US-ASCII).</span></span><a href="#l779"></a>
<span id="l780">    <span class="c"># @keyparam xml_declaration Controls if an XML declaration should</span></span><a href="#l780"></a>
<span id="l781">    <span class="c">#     be added to the file.  Use False for never, True for always,</span></span><a href="#l781"></a>
<span id="l782">    <span class="c">#     None for only if not US-ASCII or UTF-8.  None is default.</span></span><a href="#l782"></a>
<span id="l783">    <span class="c"># @keyparam default_namespace Sets the default XML namespace (for &quot;xmlns&quot;).</span></span><a href="#l783"></a>
<span id="l784">    <span class="c"># @keyparam method Optional output method (&quot;xml&quot;, &quot;html&quot;, &quot;text&quot; or</span></span><a href="#l784"></a>
<span id="l785">    <span class="c">#     &quot;c14n&quot;; default is &quot;xml&quot;).</span></span><a href="#l785"></a>
<span id="l786"></span><a href="#l786"></a>
<span id="l787">    <span class="k">def</span> <span class="nf">write</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">file_or_filename</span><span class="p">,</span></span><a href="#l787"></a>
<span id="l788">              <span class="c"># keyword arguments</span></span><a href="#l788"></a>
<span id="l789">              <span class="n">encoding</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></span><a href="#l789"></a>
<span id="l790">              <span class="n">xml_declaration</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></span><a href="#l790"></a>
<span id="l791">              <span class="n">default_namespace</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></span><a href="#l791"></a>
<span id="l792">              <span class="n">method</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l792"></a>
<span id="l793">        <span class="c"># assert self._root is not None</span></span><a href="#l793"></a>
<span id="l794">        <span class="k">if</span> <span class="ow">not</span> <span class="n">method</span><span class="p">:</span></span><a href="#l794"></a>
<span id="l795">            <span class="n">method</span> <span class="o">=</span> <span class="s">&quot;xml&quot;</span></span><a href="#l795"></a>
<span id="l796">        <span class="k">elif</span> <span class="n">method</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">_serialize</span><span class="p">:</span></span><a href="#l796"></a>
<span id="l797">            <span class="c"># FIXME: raise an ImportError for c14n if ElementC14N is missing?</span></span><a href="#l797"></a>
<span id="l798">            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s">&quot;unknown method </span><span class="si">%r</span><span class="s">&quot;</span> <span class="o">%</span> <span class="n">method</span><span class="p">)</span></span><a href="#l798"></a>
<span id="l799">        <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">file_or_filename</span><span class="p">,</span> <span class="s">&quot;write&quot;</span><span class="p">):</span></span><a href="#l799"></a>
<span id="l800">            <span class="nb">file</span> <span class="o">=</span> <span class="n">file_or_filename</span></span><a href="#l800"></a>
<span id="l801">        <span class="k">else</span><span class="p">:</span></span><a href="#l801"></a>
<span id="l802">            <span class="nb">file</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">file_or_filename</span><span class="p">,</span> <span class="s">&quot;wb&quot;</span><span class="p">)</span></span><a href="#l802"></a>
<span id="l803">        <span class="n">write</span> <span class="o">=</span> <span class="nb">file</span><span class="o">.</span><span class="n">write</span></span><a href="#l803"></a>
<span id="l804">        <span class="k">if</span> <span class="ow">not</span> <span class="n">encoding</span><span class="p">:</span></span><a href="#l804"></a>
<span id="l805">            <span class="k">if</span> <span class="n">method</span> <span class="o">==</span> <span class="s">&quot;c14n&quot;</span><span class="p">:</span></span><a href="#l805"></a>
<span id="l806">                <span class="n">encoding</span> <span class="o">=</span> <span class="s">&quot;utf-8&quot;</span></span><a href="#l806"></a>
<span id="l807">            <span class="k">else</span><span class="p">:</span></span><a href="#l807"></a>
<span id="l808">                <span class="n">encoding</span> <span class="o">=</span> <span class="s">&quot;us-ascii&quot;</span></span><a href="#l808"></a>
<span id="l809">        <span class="k">elif</span> <span class="n">xml_declaration</span> <span class="ow">or</span> <span class="p">(</span><span class="n">xml_declaration</span> <span class="ow">is</span> <span class="bp">None</span> <span class="ow">and</span></span><a href="#l809"></a>
<span id="l810">                                 <span class="n">encoding</span> <span class="ow">not</span> <span class="ow">in</span> <span class="p">(</span><span class="s">&quot;utf-8&quot;</span><span class="p">,</span> <span class="s">&quot;us-ascii&quot;</span><span class="p">)):</span></span><a href="#l810"></a>
<span id="l811">            <span class="k">if</span> <span class="n">method</span> <span class="o">==</span> <span class="s">&quot;xml&quot;</span><span class="p">:</span></span><a href="#l811"></a>
<span id="l812">                <span class="n">write</span><span class="p">(</span><span class="s">&quot;&lt;?xml version=&#39;1.0&#39; encoding=&#39;</span><span class="si">%s</span><span class="s">&#39;?&gt;</span><span class="se">\n</span><span class="s">&quot;</span> <span class="o">%</span> <span class="n">encoding</span><span class="p">)</span></span><a href="#l812"></a>
<span id="l813">        <span class="k">if</span> <span class="n">method</span> <span class="o">==</span> <span class="s">&quot;text&quot;</span><span class="p">:</span></span><a href="#l813"></a>
<span id="l814">            <span class="n">_serialize_text</span><span class="p">(</span><span class="n">write</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_root</span><span class="p">,</span> <span class="n">encoding</span><span class="p">)</span></span><a href="#l814"></a>
<span id="l815">        <span class="k">else</span><span class="p">:</span></span><a href="#l815"></a>
<span id="l816">            <span class="n">qnames</span><span class="p">,</span> <span class="n">namespaces</span> <span class="o">=</span> <span class="n">_namespaces</span><span class="p">(</span></span><a href="#l816"></a>
<span id="l817">                <span class="bp">self</span><span class="o">.</span><span class="n">_root</span><span class="p">,</span> <span class="n">encoding</span><span class="p">,</span> <span class="n">default_namespace</span></span><a href="#l817"></a>
<span id="l818">                <span class="p">)</span></span><a href="#l818"></a>
<span id="l819">            <span class="n">serialize</span> <span class="o">=</span> <span class="n">_serialize</span><span class="p">[</span><span class="n">method</span><span class="p">]</span></span><a href="#l819"></a>
<span id="l820">            <span class="n">serialize</span><span class="p">(</span><span class="n">write</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_root</span><span class="p">,</span> <span class="n">encoding</span><span class="p">,</span> <span class="n">qnames</span><span class="p">,</span> <span class="n">namespaces</span><span class="p">)</span></span><a href="#l820"></a>
<span id="l821">        <span class="k">if</span> <span class="n">file_or_filename</span> <span class="ow">is</span> <span class="ow">not</span> <span class="nb">file</span><span class="p">:</span></span><a href="#l821"></a>
<span id="l822">            <span class="nb">file</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></span><a href="#l822"></a>
<span id="l823"></span><a href="#l823"></a>
<span id="l824">    <span class="k">def</span> <span class="nf">write_c14n</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">file</span><span class="p">):</span></span><a href="#l824"></a>
<span id="l825">        <span class="c"># lxml.etree compatibility.  use output method instead</span></span><a href="#l825"></a>
<span id="l826">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="nb">file</span><span class="p">,</span> <span class="n">method</span><span class="o">=</span><span class="s">&quot;c14n&quot;</span><span class="p">)</span></span><a href="#l826"></a>
<span id="l827"></span><a href="#l827"></a>
<span id="l828"><span class="c"># --------------------------------------------------------------------</span></span><a href="#l828"></a>
<span id="l829"><span class="c"># serialization support</span></span><a href="#l829"></a>
<span id="l830"></span><a href="#l830"></a>
<span id="l831"><span class="k">def</span> <span class="nf">_namespaces</span><span class="p">(</span><span class="n">elem</span><span class="p">,</span> <span class="n">encoding</span><span class="p">,</span> <span class="n">default_namespace</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l831"></a>
<span id="l832">    <span class="c"># identify namespaces used in this tree</span></span><a href="#l832"></a>
<span id="l833"></span><a href="#l833"></a>
<span id="l834">    <span class="c"># maps qnames to *encoded* prefix:local names</span></span><a href="#l834"></a>
<span id="l835">    <span class="n">qnames</span> <span class="o">=</span> <span class="p">{</span><span class="bp">None</span><span class="p">:</span> <span class="bp">None</span><span class="p">}</span></span><a href="#l835"></a>
<span id="l836"></span><a href="#l836"></a>
<span id="l837">    <span class="c"># maps uri:s to prefixes</span></span><a href="#l837"></a>
<span id="l838">    <span class="n">namespaces</span> <span class="o">=</span> <span class="p">{}</span></span><a href="#l838"></a>
<span id="l839">    <span class="k">if</span> <span class="n">default_namespace</span><span class="p">:</span></span><a href="#l839"></a>
<span id="l840">        <span class="n">namespaces</span><span class="p">[</span><span class="n">default_namespace</span><span class="p">]</span> <span class="o">=</span> <span class="s">&quot;&quot;</span></span><a href="#l840"></a>
<span id="l841"></span><a href="#l841"></a>
<span id="l842">    <span class="k">def</span> <span class="nf">encode</span><span class="p">(</span><span class="n">text</span><span class="p">):</span></span><a href="#l842"></a>
<span id="l843">        <span class="k">return</span> <span class="n">text</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="n">encoding</span><span class="p">)</span></span><a href="#l843"></a>
<span id="l844"></span><a href="#l844"></a>
<span id="l845">    <span class="k">def</span> <span class="nf">add_qname</span><span class="p">(</span><span class="n">qname</span><span class="p">):</span></span><a href="#l845"></a>
<span id="l846">        <span class="c"># calculate serialized qname representation</span></span><a href="#l846"></a>
<span id="l847">        <span class="k">try</span><span class="p">:</span></span><a href="#l847"></a>
<span id="l848">            <span class="k">if</span> <span class="n">qname</span><span class="p">[:</span><span class="mi">1</span><span class="p">]</span> <span class="o">==</span> <span class="s">&quot;{&quot;</span><span class="p">:</span></span><a href="#l848"></a>
<span id="l849">                <span class="n">uri</span><span class="p">,</span> <span class="n">tag</span> <span class="o">=</span> <span class="n">qname</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span><span class="o">.</span><span class="n">rsplit</span><span class="p">(</span><span class="s">&quot;}&quot;</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span></span><a href="#l849"></a>
<span id="l850">                <span class="n">prefix</span> <span class="o">=</span> <span class="n">namespaces</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">uri</span><span class="p">)</span></span><a href="#l850"></a>
<span id="l851">                <span class="k">if</span> <span class="n">prefix</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l851"></a>
<span id="l852">                    <span class="n">prefix</span> <span class="o">=</span> <span class="n">_namespace_map</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">uri</span><span class="p">)</span></span><a href="#l852"></a>
<span id="l853">                    <span class="k">if</span> <span class="n">prefix</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l853"></a>
<span id="l854">                        <span class="n">prefix</span> <span class="o">=</span> <span class="s">&quot;ns</span><span class="si">%d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="nb">len</span><span class="p">(</span><span class="n">namespaces</span><span class="p">)</span></span><a href="#l854"></a>
<span id="l855">                    <span class="k">if</span> <span class="n">prefix</span> <span class="o">!=</span> <span class="s">&quot;xml&quot;</span><span class="p">:</span></span><a href="#l855"></a>
<span id="l856">                        <span class="n">namespaces</span><span class="p">[</span><span class="n">uri</span><span class="p">]</span> <span class="o">=</span> <span class="n">prefix</span></span><a href="#l856"></a>
<span id="l857">                <span class="k">if</span> <span class="n">prefix</span><span class="p">:</span></span><a href="#l857"></a>
<span id="l858">                    <span class="n">qnames</span><span class="p">[</span><span class="n">qname</span><span class="p">]</span> <span class="o">=</span> <span class="n">encode</span><span class="p">(</span><span class="s">&quot;</span><span class="si">%s</span><span class="s">:</span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">prefix</span><span class="p">,</span> <span class="n">tag</span><span class="p">))</span></span><a href="#l858"></a>
<span id="l859">                <span class="k">else</span><span class="p">:</span></span><a href="#l859"></a>
<span id="l860">                    <span class="n">qnames</span><span class="p">[</span><span class="n">qname</span><span class="p">]</span> <span class="o">=</span> <span class="n">encode</span><span class="p">(</span><span class="n">tag</span><span class="p">)</span> <span class="c"># default element</span></span><a href="#l860"></a>
<span id="l861">            <span class="k">else</span><span class="p">:</span></span><a href="#l861"></a>
<span id="l862">                <span class="k">if</span> <span class="n">default_namespace</span><span class="p">:</span></span><a href="#l862"></a>
<span id="l863">                    <span class="c"># FIXME: can this be handled in XML 1.0?</span></span><a href="#l863"></a>
<span id="l864">                    <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span></span><a href="#l864"></a>
<span id="l865">                        <span class="s">&quot;cannot use non-qualified names with &quot;</span></span><a href="#l865"></a>
<span id="l866">                        <span class="s">&quot;default_namespace option&quot;</span></span><a href="#l866"></a>
<span id="l867">                        <span class="p">)</span></span><a href="#l867"></a>
<span id="l868">                <span class="n">qnames</span><span class="p">[</span><span class="n">qname</span><span class="p">]</span> <span class="o">=</span> <span class="n">encode</span><span class="p">(</span><span class="n">qname</span><span class="p">)</span></span><a href="#l868"></a>
<span id="l869">        <span class="k">except</span> <span class="ne">TypeError</span><span class="p">:</span></span><a href="#l869"></a>
<span id="l870">            <span class="n">_raise_serialization_error</span><span class="p">(</span><span class="n">qname</span><span class="p">)</span></span><a href="#l870"></a>
<span id="l871"></span><a href="#l871"></a>
<span id="l872">    <span class="c"># populate qname and namespaces table</span></span><a href="#l872"></a>
<span id="l873">    <span class="k">try</span><span class="p">:</span></span><a href="#l873"></a>
<span id="l874">        <span class="n">iterate</span> <span class="o">=</span> <span class="n">elem</span><span class="o">.</span><span class="n">iter</span></span><a href="#l874"></a>
<span id="l875">    <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span></span><a href="#l875"></a>
<span id="l876">        <span class="n">iterate</span> <span class="o">=</span> <span class="n">elem</span><span class="o">.</span><span class="n">getiterator</span> <span class="c"># cET compatibility</span></span><a href="#l876"></a>
<span id="l877">    <span class="k">for</span> <span class="n">elem</span> <span class="ow">in</span> <span class="n">iterate</span><span class="p">():</span></span><a href="#l877"></a>
<span id="l878">        <span class="n">tag</span> <span class="o">=</span> <span class="n">elem</span><span class="o">.</span><span class="n">tag</span></span><a href="#l878"></a>
<span id="l879">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">tag</span><span class="p">,</span> <span class="n">QName</span><span class="p">):</span></span><a href="#l879"></a>
<span id="l880">            <span class="k">if</span> <span class="n">tag</span><span class="o">.</span><span class="n">text</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">qnames</span><span class="p">:</span></span><a href="#l880"></a>
<span id="l881">                <span class="n">add_qname</span><span class="p">(</span><span class="n">tag</span><span class="o">.</span><span class="n">text</span><span class="p">)</span></span><a href="#l881"></a>
<span id="l882">        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">tag</span><span class="p">,</span> <span class="nb">basestring</span><span class="p">):</span></span><a href="#l882"></a>
<span id="l883">            <span class="k">if</span> <span class="n">tag</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">qnames</span><span class="p">:</span></span><a href="#l883"></a>
<span id="l884">                <span class="n">add_qname</span><span class="p">(</span><span class="n">tag</span><span class="p">)</span></span><a href="#l884"></a>
<span id="l885">        <span class="k">elif</span> <span class="n">tag</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span> <span class="ow">and</span> <span class="n">tag</span> <span class="ow">is</span> <span class="ow">not</span> <span class="n">Comment</span> <span class="ow">and</span> <span class="n">tag</span> <span class="ow">is</span> <span class="ow">not</span> <span class="n">PI</span><span class="p">:</span></span><a href="#l885"></a>
<span id="l886">            <span class="n">_raise_serialization_error</span><span class="p">(</span><span class="n">tag</span><span class="p">)</span></span><a href="#l886"></a>
<span id="l887">        <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">elem</span><span class="o">.</span><span class="n">items</span><span class="p">():</span></span><a href="#l887"></a>
<span id="l888">            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">QName</span><span class="p">):</span></span><a href="#l888"></a>
<span id="l889">                <span class="n">key</span> <span class="o">=</span> <span class="n">key</span><span class="o">.</span><span class="n">text</span></span><a href="#l889"></a>
<span id="l890">            <span class="k">if</span> <span class="n">key</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">qnames</span><span class="p">:</span></span><a href="#l890"></a>
<span id="l891">                <span class="n">add_qname</span><span class="p">(</span><span class="n">key</span><span class="p">)</span></span><a href="#l891"></a>
<span id="l892">            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="n">QName</span><span class="p">)</span> <span class="ow">and</span> <span class="n">value</span><span class="o">.</span><span class="n">text</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">qnames</span><span class="p">:</span></span><a href="#l892"></a>
<span id="l893">                <span class="n">add_qname</span><span class="p">(</span><span class="n">value</span><span class="o">.</span><span class="n">text</span><span class="p">)</span></span><a href="#l893"></a>
<span id="l894">        <span class="n">text</span> <span class="o">=</span> <span class="n">elem</span><span class="o">.</span><span class="n">text</span></span><a href="#l894"></a>
<span id="l895">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="n">QName</span><span class="p">)</span> <span class="ow">and</span> <span class="n">text</span><span class="o">.</span><span class="n">text</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">qnames</span><span class="p">:</span></span><a href="#l895"></a>
<span id="l896">            <span class="n">add_qname</span><span class="p">(</span><span class="n">text</span><span class="o">.</span><span class="n">text</span><span class="p">)</span></span><a href="#l896"></a>
<span id="l897">    <span class="k">return</span> <span class="n">qnames</span><span class="p">,</span> <span class="n">namespaces</span></span><a href="#l897"></a>
<span id="l898"></span><a href="#l898"></a>
<span id="l899"><span class="k">def</span> <span class="nf">_serialize_xml</span><span class="p">(</span><span class="n">write</span><span class="p">,</span> <span class="n">elem</span><span class="p">,</span> <span class="n">encoding</span><span class="p">,</span> <span class="n">qnames</span><span class="p">,</span> <span class="n">namespaces</span><span class="p">):</span></span><a href="#l899"></a>
<span id="l900">    <span class="n">tag</span> <span class="o">=</span> <span class="n">elem</span><span class="o">.</span><span class="n">tag</span></span><a href="#l900"></a>
<span id="l901">    <span class="n">text</span> <span class="o">=</span> <span class="n">elem</span><span class="o">.</span><span class="n">text</span></span><a href="#l901"></a>
<span id="l902">    <span class="k">if</span> <span class="n">tag</span> <span class="ow">is</span> <span class="n">Comment</span><span class="p">:</span></span><a href="#l902"></a>
<span id="l903">        <span class="n">write</span><span class="p">(</span><span class="s">&quot;&lt;!--</span><span class="si">%s</span><span class="s">--&gt;&quot;</span> <span class="o">%</span> <span class="n">_encode</span><span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="n">encoding</span><span class="p">))</span></span><a href="#l903"></a>
<span id="l904">    <span class="k">elif</span> <span class="n">tag</span> <span class="ow">is</span> <span class="n">ProcessingInstruction</span><span class="p">:</span></span><a href="#l904"></a>
<span id="l905">        <span class="n">write</span><span class="p">(</span><span class="s">&quot;&lt;?</span><span class="si">%s</span><span class="s">?&gt;&quot;</span> <span class="o">%</span> <span class="n">_encode</span><span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="n">encoding</span><span class="p">))</span></span><a href="#l905"></a>
<span id="l906">    <span class="k">else</span><span class="p">:</span></span><a href="#l906"></a>
<span id="l907">        <span class="n">tag</span> <span class="o">=</span> <span class="n">qnames</span><span class="p">[</span><span class="n">tag</span><span class="p">]</span></span><a href="#l907"></a>
<span id="l908">        <span class="k">if</span> <span class="n">tag</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l908"></a>
<span id="l909">            <span class="k">if</span> <span class="n">text</span><span class="p">:</span></span><a href="#l909"></a>
<span id="l910">                <span class="n">write</span><span class="p">(</span><span class="n">_escape_cdata</span><span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="n">encoding</span><span class="p">))</span></span><a href="#l910"></a>
<span id="l911">            <span class="k">for</span> <span class="n">e</span> <span class="ow">in</span> <span class="n">elem</span><span class="p">:</span></span><a href="#l911"></a>
<span id="l912">                <span class="n">_serialize_xml</span><span class="p">(</span><span class="n">write</span><span class="p">,</span> <span class="n">e</span><span class="p">,</span> <span class="n">encoding</span><span class="p">,</span> <span class="n">qnames</span><span class="p">,</span> <span class="bp">None</span><span class="p">)</span></span><a href="#l912"></a>
<span id="l913">        <span class="k">else</span><span class="p">:</span></span><a href="#l913"></a>
<span id="l914">            <span class="n">write</span><span class="p">(</span><span class="s">&quot;&lt;&quot;</span> <span class="o">+</span> <span class="n">tag</span><span class="p">)</span></span><a href="#l914"></a>
<span id="l915">            <span class="n">items</span> <span class="o">=</span> <span class="n">elem</span><span class="o">.</span><span class="n">items</span><span class="p">()</span></span><a href="#l915"></a>
<span id="l916">            <span class="k">if</span> <span class="n">items</span> <span class="ow">or</span> <span class="n">namespaces</span><span class="p">:</span></span><a href="#l916"></a>
<span id="l917">                <span class="k">if</span> <span class="n">namespaces</span><span class="p">:</span></span><a href="#l917"></a>
<span id="l918">                    <span class="k">for</span> <span class="n">v</span><span class="p">,</span> <span class="n">k</span> <span class="ow">in</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">namespaces</span><span class="o">.</span><span class="n">items</span><span class="p">(),</span></span><a href="#l918"></a>
<span id="l919">                                       <span class="n">key</span><span class="o">=</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">x</span><span class="p">[</span><span class="mi">1</span><span class="p">]):</span>  <span class="c"># sort on prefix</span></span><a href="#l919"></a>
<span id="l920">                        <span class="k">if</span> <span class="n">k</span><span class="p">:</span></span><a href="#l920"></a>
<span id="l921">                            <span class="n">k</span> <span class="o">=</span> <span class="s">&quot;:&quot;</span> <span class="o">+</span> <span class="n">k</span></span><a href="#l921"></a>
<span id="l922">                        <span class="n">write</span><span class="p">(</span><span class="s">&quot; xmlns</span><span class="si">%s</span><span class="s">=</span><span class="se">\&quot;</span><span class="si">%s</span><span class="se">\&quot;</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span></span><a href="#l922"></a>
<span id="l923">                            <span class="n">k</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="n">encoding</span><span class="p">),</span></span><a href="#l923"></a>
<span id="l924">                            <span class="n">_escape_attrib</span><span class="p">(</span><span class="n">v</span><span class="p">,</span> <span class="n">encoding</span><span class="p">)</span></span><a href="#l924"></a>
<span id="l925">                            <span class="p">))</span></span><a href="#l925"></a>
<span id="l926">                <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">items</span><span class="p">):</span>  <span class="c"># lexical order</span></span><a href="#l926"></a>
<span id="l927">                    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">k</span><span class="p">,</span> <span class="n">QName</span><span class="p">):</span></span><a href="#l927"></a>
<span id="l928">                        <span class="n">k</span> <span class="o">=</span> <span class="n">k</span><span class="o">.</span><span class="n">text</span></span><a href="#l928"></a>
<span id="l929">                    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">v</span><span class="p">,</span> <span class="n">QName</span><span class="p">):</span></span><a href="#l929"></a>
<span id="l930">                        <span class="n">v</span> <span class="o">=</span> <span class="n">qnames</span><span class="p">[</span><span class="n">v</span><span class="o">.</span><span class="n">text</span><span class="p">]</span></span><a href="#l930"></a>
<span id="l931">                    <span class="k">else</span><span class="p">:</span></span><a href="#l931"></a>
<span id="l932">                        <span class="n">v</span> <span class="o">=</span> <span class="n">_escape_attrib</span><span class="p">(</span><span class="n">v</span><span class="p">,</span> <span class="n">encoding</span><span class="p">)</span></span><a href="#l932"></a>
<span id="l933">                    <span class="n">write</span><span class="p">(</span><span class="s">&quot; </span><span class="si">%s</span><span class="s">=</span><span class="se">\&quot;</span><span class="si">%s</span><span class="se">\&quot;</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">qnames</span><span class="p">[</span><span class="n">k</span><span class="p">],</span> <span class="n">v</span><span class="p">))</span></span><a href="#l933"></a>
<span id="l934">            <span class="k">if</span> <span class="n">text</span> <span class="ow">or</span> <span class="nb">len</span><span class="p">(</span><span class="n">elem</span><span class="p">):</span></span><a href="#l934"></a>
<span id="l935">                <span class="n">write</span><span class="p">(</span><span class="s">&quot;&gt;&quot;</span><span class="p">)</span></span><a href="#l935"></a>
<span id="l936">                <span class="k">if</span> <span class="n">text</span><span class="p">:</span></span><a href="#l936"></a>
<span id="l937">                    <span class="n">write</span><span class="p">(</span><span class="n">_escape_cdata</span><span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="n">encoding</span><span class="p">))</span></span><a href="#l937"></a>
<span id="l938">                <span class="k">for</span> <span class="n">e</span> <span class="ow">in</span> <span class="n">elem</span><span class="p">:</span></span><a href="#l938"></a>
<span id="l939">                    <span class="n">_serialize_xml</span><span class="p">(</span><span class="n">write</span><span class="p">,</span> <span class="n">e</span><span class="p">,</span> <span class="n">encoding</span><span class="p">,</span> <span class="n">qnames</span><span class="p">,</span> <span class="bp">None</span><span class="p">)</span></span><a href="#l939"></a>
<span id="l940">                <span class="n">write</span><span class="p">(</span><span class="s">&quot;&lt;/&quot;</span> <span class="o">+</span> <span class="n">tag</span> <span class="o">+</span> <span class="s">&quot;&gt;&quot;</span><span class="p">)</span></span><a href="#l940"></a>
<span id="l941">            <span class="k">else</span><span class="p">:</span></span><a href="#l941"></a>
<span id="l942">                <span class="n">write</span><span class="p">(</span><span class="s">&quot; /&gt;&quot;</span><span class="p">)</span></span><a href="#l942"></a>
<span id="l943">    <span class="k">if</span> <span class="n">elem</span><span class="o">.</span><span class="n">tail</span><span class="p">:</span></span><a href="#l943"></a>
<span id="l944">        <span class="n">write</span><span class="p">(</span><span class="n">_escape_cdata</span><span class="p">(</span><span class="n">elem</span><span class="o">.</span><span class="n">tail</span><span class="p">,</span> <span class="n">encoding</span><span class="p">))</span></span><a href="#l944"></a>
<span id="l945"></span><a href="#l945"></a>
<span id="l946"><span class="n">HTML_EMPTY</span> <span class="o">=</span> <span class="p">(</span><span class="s">&quot;area&quot;</span><span class="p">,</span> <span class="s">&quot;base&quot;</span><span class="p">,</span> <span class="s">&quot;basefont&quot;</span><span class="p">,</span> <span class="s">&quot;br&quot;</span><span class="p">,</span> <span class="s">&quot;col&quot;</span><span class="p">,</span> <span class="s">&quot;frame&quot;</span><span class="p">,</span> <span class="s">&quot;hr&quot;</span><span class="p">,</span></span><a href="#l946"></a>
<span id="l947">              <span class="s">&quot;img&quot;</span><span class="p">,</span> <span class="s">&quot;input&quot;</span><span class="p">,</span> <span class="s">&quot;isindex&quot;</span><span class="p">,</span> <span class="s">&quot;link&quot;</span><span class="p">,</span> <span class="s">&quot;meta&quot;</span><span class="p">,</span> <span class="s">&quot;param&quot;</span><span class="p">)</span></span><a href="#l947"></a>
<span id="l948"></span><a href="#l948"></a>
<span id="l949"><span class="k">try</span><span class="p">:</span></span><a href="#l949"></a>
<span id="l950">    <span class="n">HTML_EMPTY</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">HTML_EMPTY</span><span class="p">)</span></span><a href="#l950"></a>
<span id="l951"><span class="k">except</span> <span class="ne">NameError</span><span class="p">:</span></span><a href="#l951"></a>
<span id="l952">    <span class="k">pass</span></span><a href="#l952"></a>
<span id="l953"></span><a href="#l953"></a>
<span id="l954"><span class="k">def</span> <span class="nf">_serialize_html</span><span class="p">(</span><span class="n">write</span><span class="p">,</span> <span class="n">elem</span><span class="p">,</span> <span class="n">encoding</span><span class="p">,</span> <span class="n">qnames</span><span class="p">,</span> <span class="n">namespaces</span><span class="p">):</span></span><a href="#l954"></a>
<span id="l955">    <span class="n">tag</span> <span class="o">=</span> <span class="n">elem</span><span class="o">.</span><span class="n">tag</span></span><a href="#l955"></a>
<span id="l956">    <span class="n">text</span> <span class="o">=</span> <span class="n">elem</span><span class="o">.</span><span class="n">text</span></span><a href="#l956"></a>
<span id="l957">    <span class="k">if</span> <span class="n">tag</span> <span class="ow">is</span> <span class="n">Comment</span><span class="p">:</span></span><a href="#l957"></a>
<span id="l958">        <span class="n">write</span><span class="p">(</span><span class="s">&quot;&lt;!--</span><span class="si">%s</span><span class="s">--&gt;&quot;</span> <span class="o">%</span> <span class="n">_escape_cdata</span><span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="n">encoding</span><span class="p">))</span></span><a href="#l958"></a>
<span id="l959">    <span class="k">elif</span> <span class="n">tag</span> <span class="ow">is</span> <span class="n">ProcessingInstruction</span><span class="p">:</span></span><a href="#l959"></a>
<span id="l960">        <span class="n">write</span><span class="p">(</span><span class="s">&quot;&lt;?</span><span class="si">%s</span><span class="s">?&gt;&quot;</span> <span class="o">%</span> <span class="n">_escape_cdata</span><span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="n">encoding</span><span class="p">))</span></span><a href="#l960"></a>
<span id="l961">    <span class="k">else</span><span class="p">:</span></span><a href="#l961"></a>
<span id="l962">        <span class="n">tag</span> <span class="o">=</span> <span class="n">qnames</span><span class="p">[</span><span class="n">tag</span><span class="p">]</span></span><a href="#l962"></a>
<span id="l963">        <span class="k">if</span> <span class="n">tag</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l963"></a>
<span id="l964">            <span class="k">if</span> <span class="n">text</span><span class="p">:</span></span><a href="#l964"></a>
<span id="l965">                <span class="n">write</span><span class="p">(</span><span class="n">_escape_cdata</span><span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="n">encoding</span><span class="p">))</span></span><a href="#l965"></a>
<span id="l966">            <span class="k">for</span> <span class="n">e</span> <span class="ow">in</span> <span class="n">elem</span><span class="p">:</span></span><a href="#l966"></a>
<span id="l967">                <span class="n">_serialize_html</span><span class="p">(</span><span class="n">write</span><span class="p">,</span> <span class="n">e</span><span class="p">,</span> <span class="n">encoding</span><span class="p">,</span> <span class="n">qnames</span><span class="p">,</span> <span class="bp">None</span><span class="p">)</span></span><a href="#l967"></a>
<span id="l968">        <span class="k">else</span><span class="p">:</span></span><a href="#l968"></a>
<span id="l969">            <span class="n">write</span><span class="p">(</span><span class="s">&quot;&lt;&quot;</span> <span class="o">+</span> <span class="n">tag</span><span class="p">)</span></span><a href="#l969"></a>
<span id="l970">            <span class="n">items</span> <span class="o">=</span> <span class="n">elem</span><span class="o">.</span><span class="n">items</span><span class="p">()</span></span><a href="#l970"></a>
<span id="l971">            <span class="k">if</span> <span class="n">items</span> <span class="ow">or</span> <span class="n">namespaces</span><span class="p">:</span></span><a href="#l971"></a>
<span id="l972">                <span class="k">if</span> <span class="n">namespaces</span><span class="p">:</span></span><a href="#l972"></a>
<span id="l973">                    <span class="k">for</span> <span class="n">v</span><span class="p">,</span> <span class="n">k</span> <span class="ow">in</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">namespaces</span><span class="o">.</span><span class="n">items</span><span class="p">(),</span></span><a href="#l973"></a>
<span id="l974">                                       <span class="n">key</span><span class="o">=</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">x</span><span class="p">[</span><span class="mi">1</span><span class="p">]):</span>  <span class="c"># sort on prefix</span></span><a href="#l974"></a>
<span id="l975">                        <span class="k">if</span> <span class="n">k</span><span class="p">:</span></span><a href="#l975"></a>
<span id="l976">                            <span class="n">k</span> <span class="o">=</span> <span class="s">&quot;:&quot;</span> <span class="o">+</span> <span class="n">k</span></span><a href="#l976"></a>
<span id="l977">                        <span class="n">write</span><span class="p">(</span><span class="s">&quot; xmlns</span><span class="si">%s</span><span class="s">=</span><span class="se">\&quot;</span><span class="si">%s</span><span class="se">\&quot;</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span></span><a href="#l977"></a>
<span id="l978">                            <span class="n">k</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="n">encoding</span><span class="p">),</span></span><a href="#l978"></a>
<span id="l979">                            <span class="n">_escape_attrib</span><span class="p">(</span><span class="n">v</span><span class="p">,</span> <span class="n">encoding</span><span class="p">)</span></span><a href="#l979"></a>
<span id="l980">                            <span class="p">))</span></span><a href="#l980"></a>
<span id="l981">                <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">items</span><span class="p">):</span>  <span class="c"># lexical order</span></span><a href="#l981"></a>
<span id="l982">                    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">k</span><span class="p">,</span> <span class="n">QName</span><span class="p">):</span></span><a href="#l982"></a>
<span id="l983">                        <span class="n">k</span> <span class="o">=</span> <span class="n">k</span><span class="o">.</span><span class="n">text</span></span><a href="#l983"></a>
<span id="l984">                    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">v</span><span class="p">,</span> <span class="n">QName</span><span class="p">):</span></span><a href="#l984"></a>
<span id="l985">                        <span class="n">v</span> <span class="o">=</span> <span class="n">qnames</span><span class="p">[</span><span class="n">v</span><span class="o">.</span><span class="n">text</span><span class="p">]</span></span><a href="#l985"></a>
<span id="l986">                    <span class="k">else</span><span class="p">:</span></span><a href="#l986"></a>
<span id="l987">                        <span class="n">v</span> <span class="o">=</span> <span class="n">_escape_attrib_html</span><span class="p">(</span><span class="n">v</span><span class="p">,</span> <span class="n">encoding</span><span class="p">)</span></span><a href="#l987"></a>
<span id="l988">                    <span class="c"># FIXME: handle boolean attributes</span></span><a href="#l988"></a>
<span id="l989">                    <span class="n">write</span><span class="p">(</span><span class="s">&quot; </span><span class="si">%s</span><span class="s">=</span><span class="se">\&quot;</span><span class="si">%s</span><span class="se">\&quot;</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">qnames</span><span class="p">[</span><span class="n">k</span><span class="p">],</span> <span class="n">v</span><span class="p">))</span></span><a href="#l989"></a>
<span id="l990">            <span class="n">write</span><span class="p">(</span><span class="s">&quot;&gt;&quot;</span><span class="p">)</span></span><a href="#l990"></a>
<span id="l991">            <span class="n">ltag</span> <span class="o">=</span> <span class="n">tag</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span></span><a href="#l991"></a>
<span id="l992">            <span class="k">if</span> <span class="n">text</span><span class="p">:</span></span><a href="#l992"></a>
<span id="l993">                <span class="k">if</span> <span class="n">ltag</span> <span class="o">==</span> <span class="s">&quot;script&quot;</span> <span class="ow">or</span> <span class="n">ltag</span> <span class="o">==</span> <span class="s">&quot;style&quot;</span><span class="p">:</span></span><a href="#l993"></a>
<span id="l994">                    <span class="n">write</span><span class="p">(</span><span class="n">_encode</span><span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="n">encoding</span><span class="p">))</span></span><a href="#l994"></a>
<span id="l995">                <span class="k">else</span><span class="p">:</span></span><a href="#l995"></a>
<span id="l996">                    <span class="n">write</span><span class="p">(</span><span class="n">_escape_cdata</span><span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="n">encoding</span><span class="p">))</span></span><a href="#l996"></a>
<span id="l997">            <span class="k">for</span> <span class="n">e</span> <span class="ow">in</span> <span class="n">elem</span><span class="p">:</span></span><a href="#l997"></a>
<span id="l998">                <span class="n">_serialize_html</span><span class="p">(</span><span class="n">write</span><span class="p">,</span> <span class="n">e</span><span class="p">,</span> <span class="n">encoding</span><span class="p">,</span> <span class="n">qnames</span><span class="p">,</span> <span class="bp">None</span><span class="p">)</span></span><a href="#l998"></a>
<span id="l999">            <span class="k">if</span> <span class="n">ltag</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">HTML_EMPTY</span><span class="p">:</span></span><a href="#l999"></a>
<span id="l1000">                <span class="n">write</span><span class="p">(</span><span class="s">&quot;&lt;/&quot;</span> <span class="o">+</span> <span class="n">tag</span> <span class="o">+</span> <span class="s">&quot;&gt;&quot;</span><span class="p">)</span></span><a href="#l1000"></a>
<span id="l1001">    <span class="k">if</span> <span class="n">elem</span><span class="o">.</span><span class="n">tail</span><span class="p">:</span></span><a href="#l1001"></a>
<span id="l1002">        <span class="n">write</span><span class="p">(</span><span class="n">_escape_cdata</span><span class="p">(</span><span class="n">elem</span><span class="o">.</span><span class="n">tail</span><span class="p">,</span> <span class="n">encoding</span><span class="p">))</span></span><a href="#l1002"></a>
<span id="l1003"></span><a href="#l1003"></a>
<span id="l1004"><span class="k">def</span> <span class="nf">_serialize_text</span><span class="p">(</span><span class="n">write</span><span class="p">,</span> <span class="n">elem</span><span class="p">,</span> <span class="n">encoding</span><span class="p">):</span></span><a href="#l1004"></a>
<span id="l1005">    <span class="k">for</span> <span class="n">part</span> <span class="ow">in</span> <span class="n">elem</span><span class="o">.</span><span class="n">itertext</span><span class="p">():</span></span><a href="#l1005"></a>
<span id="l1006">        <span class="n">write</span><span class="p">(</span><span class="n">part</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="n">encoding</span><span class="p">))</span></span><a href="#l1006"></a>
<span id="l1007">    <span class="k">if</span> <span class="n">elem</span><span class="o">.</span><span class="n">tail</span><span class="p">:</span></span><a href="#l1007"></a>
<span id="l1008">        <span class="n">write</span><span class="p">(</span><span class="n">elem</span><span class="o">.</span><span class="n">tail</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="n">encoding</span><span class="p">))</span></span><a href="#l1008"></a>
<span id="l1009"></span><a href="#l1009"></a>
<span id="l1010"><span class="n">_serialize</span> <span class="o">=</span> <span class="p">{</span></span><a href="#l1010"></a>
<span id="l1011">    <span class="s">&quot;xml&quot;</span><span class="p">:</span> <span class="n">_serialize_xml</span><span class="p">,</span></span><a href="#l1011"></a>
<span id="l1012">    <span class="s">&quot;html&quot;</span><span class="p">:</span> <span class="n">_serialize_html</span><span class="p">,</span></span><a href="#l1012"></a>
<span id="l1013">    <span class="s">&quot;text&quot;</span><span class="p">:</span> <span class="n">_serialize_text</span><span class="p">,</span></span><a href="#l1013"></a>
<span id="l1014"><span class="c"># this optional method is imported at the end of the module</span></span><a href="#l1014"></a>
<span id="l1015"><span class="c">#   &quot;c14n&quot;: _serialize_c14n,</span></span><a href="#l1015"></a>
<span id="l1016"><span class="p">}</span></span><a href="#l1016"></a>
<span id="l1017"></span><a href="#l1017"></a>
<span id="l1018"><span class="c">##</span></span><a href="#l1018"></a>
<span id="l1019"><span class="c"># Registers a namespace prefix.  The registry is global, and any</span></span><a href="#l1019"></a>
<span id="l1020"><span class="c"># existing mapping for either the given prefix or the namespace URI</span></span><a href="#l1020"></a>
<span id="l1021"><span class="c"># will be removed.</span></span><a href="#l1021"></a>
<span id="l1022"><span class="c">#</span></span><a href="#l1022"></a>
<span id="l1023"><span class="c"># @param prefix Namespace prefix.</span></span><a href="#l1023"></a>
<span id="l1024"><span class="c"># @param uri Namespace uri.  Tags and attributes in this namespace</span></span><a href="#l1024"></a>
<span id="l1025"><span class="c">#     will be serialized with the given prefix, if at all possible.</span></span><a href="#l1025"></a>
<span id="l1026"><span class="c"># @exception ValueError If the prefix is reserved, or is otherwise</span></span><a href="#l1026"></a>
<span id="l1027"><span class="c">#     invalid.</span></span><a href="#l1027"></a>
<span id="l1028"></span><a href="#l1028"></a>
<span id="l1029"><span class="k">def</span> <span class="nf">register_namespace</span><span class="p">(</span><span class="n">prefix</span><span class="p">,</span> <span class="n">uri</span><span class="p">):</span></span><a href="#l1029"></a>
<span id="l1030">    <span class="k">if</span> <span class="n">re</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="s">&quot;ns\d+$&quot;</span><span class="p">,</span> <span class="n">prefix</span><span class="p">):</span></span><a href="#l1030"></a>
<span id="l1031">        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s">&quot;Prefix format reserved for internal use&quot;</span><span class="p">)</span></span><a href="#l1031"></a>
<span id="l1032">    <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">_namespace_map</span><span class="o">.</span><span class="n">items</span><span class="p">():</span></span><a href="#l1032"></a>
<span id="l1033">        <span class="k">if</span> <span class="n">k</span> <span class="o">==</span> <span class="n">uri</span> <span class="ow">or</span> <span class="n">v</span> <span class="o">==</span> <span class="n">prefix</span><span class="p">:</span></span><a href="#l1033"></a>
<span id="l1034">            <span class="k">del</span> <span class="n">_namespace_map</span><span class="p">[</span><span class="n">k</span><span class="p">]</span></span><a href="#l1034"></a>
<span id="l1035">    <span class="n">_namespace_map</span><span class="p">[</span><span class="n">uri</span><span class="p">]</span> <span class="o">=</span> <span class="n">prefix</span></span><a href="#l1035"></a>
<span id="l1036"></span><a href="#l1036"></a>
<span id="l1037"><span class="n">_namespace_map</span> <span class="o">=</span> <span class="p">{</span></span><a href="#l1037"></a>
<span id="l1038">    <span class="c"># &quot;well-known&quot; namespace prefixes</span></span><a href="#l1038"></a>
<span id="l1039">    <span class="s">&quot;http://www.w3.org/XML/1998/namespace&quot;</span><span class="p">:</span> <span class="s">&quot;xml&quot;</span><span class="p">,</span></span><a href="#l1039"></a>
<span id="l1040">    <span class="s">&quot;http://www.w3.org/1999/xhtml&quot;</span><span class="p">:</span> <span class="s">&quot;html&quot;</span><span class="p">,</span></span><a href="#l1040"></a>
<span id="l1041">    <span class="s">&quot;http://www.w3.org/1999/02/22-rdf-syntax-ns#&quot;</span><span class="p">:</span> <span class="s">&quot;rdf&quot;</span><span class="p">,</span></span><a href="#l1041"></a>
<span id="l1042">    <span class="s">&quot;http://schemas.xmlsoap.org/wsdl/&quot;</span><span class="p">:</span> <span class="s">&quot;wsdl&quot;</span><span class="p">,</span></span><a href="#l1042"></a>
<span id="l1043">    <span class="c"># xml schema</span></span><a href="#l1043"></a>
<span id="l1044">    <span class="s">&quot;http://www.w3.org/2001/XMLSchema&quot;</span><span class="p">:</span> <span class="s">&quot;xs&quot;</span><span class="p">,</span></span><a href="#l1044"></a>
<span id="l1045">    <span class="s">&quot;http://www.w3.org/2001/XMLSchema-instance&quot;</span><span class="p">:</span> <span class="s">&quot;xsi&quot;</span><span class="p">,</span></span><a href="#l1045"></a>
<span id="l1046">    <span class="c"># dublin core</span></span><a href="#l1046"></a>
<span id="l1047">    <span class="s">&quot;http://purl.org/dc/elements/1.1/&quot;</span><span class="p">:</span> <span class="s">&quot;dc&quot;</span><span class="p">,</span></span><a href="#l1047"></a>
<span id="l1048"><span class="p">}</span></span><a href="#l1048"></a>
<span id="l1049"></span><a href="#l1049"></a>
<span id="l1050"><span class="k">def</span> <span class="nf">_raise_serialization_error</span><span class="p">(</span><span class="n">text</span><span class="p">):</span></span><a href="#l1050"></a>
<span id="l1051">    <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span></span><a href="#l1051"></a>
<span id="l1052">        <span class="s">&quot;cannot serialize </span><span class="si">%r</span><span class="s"> (type </span><span class="si">%s</span><span class="s">)&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="nb">type</span><span class="p">(</span><span class="n">text</span><span class="p">)</span><span class="o">.</span><span class="n">__name__</span><span class="p">)</span></span><a href="#l1052"></a>
<span id="l1053">        <span class="p">)</span></span><a href="#l1053"></a>
<span id="l1054"></span><a href="#l1054"></a>
<span id="l1055"><span class="k">def</span> <span class="nf">_encode</span><span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="n">encoding</span><span class="p">):</span></span><a href="#l1055"></a>
<span id="l1056">    <span class="k">try</span><span class="p">:</span></span><a href="#l1056"></a>
<span id="l1057">        <span class="k">return</span> <span class="n">text</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="n">encoding</span><span class="p">,</span> <span class="s">&quot;xmlcharrefreplace&quot;</span><span class="p">)</span></span><a href="#l1057"></a>
<span id="l1058">    <span class="k">except</span> <span class="p">(</span><span class="ne">TypeError</span><span class="p">,</span> <span class="ne">AttributeError</span><span class="p">):</span></span><a href="#l1058"></a>
<span id="l1059">        <span class="n">_raise_serialization_error</span><span class="p">(</span><span class="n">text</span><span class="p">)</span></span><a href="#l1059"></a>
<span id="l1060"></span><a href="#l1060"></a>
<span id="l1061"><span class="k">def</span> <span class="nf">_escape_cdata</span><span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="n">encoding</span><span class="p">):</span></span><a href="#l1061"></a>
<span id="l1062">    <span class="c"># escape character data</span></span><a href="#l1062"></a>
<span id="l1063">    <span class="k">try</span><span class="p">:</span></span><a href="#l1063"></a>
<span id="l1064">        <span class="c"># it&#39;s worth avoiding do-nothing calls for strings that are</span></span><a href="#l1064"></a>
<span id="l1065">        <span class="c"># shorter than 500 character, or so.  assume that&#39;s, by far,</span></span><a href="#l1065"></a>
<span id="l1066">        <span class="c"># the most common case in most applications.</span></span><a href="#l1066"></a>
<span id="l1067">        <span class="k">if</span> <span class="s">&quot;&amp;&quot;</span> <span class="ow">in</span> <span class="n">text</span><span class="p">:</span></span><a href="#l1067"></a>
<span id="l1068">            <span class="n">text</span> <span class="o">=</span> <span class="n">text</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&quot;&amp;&quot;</span><span class="p">,</span> <span class="s">&quot;&amp;amp;&quot;</span><span class="p">)</span></span><a href="#l1068"></a>
<span id="l1069">        <span class="k">if</span> <span class="s">&quot;&lt;&quot;</span> <span class="ow">in</span> <span class="n">text</span><span class="p">:</span></span><a href="#l1069"></a>
<span id="l1070">            <span class="n">text</span> <span class="o">=</span> <span class="n">text</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&quot;&lt;&quot;</span><span class="p">,</span> <span class="s">&quot;&amp;lt;&quot;</span><span class="p">)</span></span><a href="#l1070"></a>
<span id="l1071">        <span class="k">if</span> <span class="s">&quot;&gt;&quot;</span> <span class="ow">in</span> <span class="n">text</span><span class="p">:</span></span><a href="#l1071"></a>
<span id="l1072">            <span class="n">text</span> <span class="o">=</span> <span class="n">text</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&quot;&gt;&quot;</span><span class="p">,</span> <span class="s">&quot;&amp;gt;&quot;</span><span class="p">)</span></span><a href="#l1072"></a>
<span id="l1073">        <span class="k">return</span> <span class="n">text</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="n">encoding</span><span class="p">,</span> <span class="s">&quot;xmlcharrefreplace&quot;</span><span class="p">)</span></span><a href="#l1073"></a>
<span id="l1074">    <span class="k">except</span> <span class="p">(</span><span class="ne">TypeError</span><span class="p">,</span> <span class="ne">AttributeError</span><span class="p">):</span></span><a href="#l1074"></a>
<span id="l1075">        <span class="n">_raise_serialization_error</span><span class="p">(</span><span class="n">text</span><span class="p">)</span></span><a href="#l1075"></a>
<span id="l1076"></span><a href="#l1076"></a>
<span id="l1077"><span class="k">def</span> <span class="nf">_escape_attrib</span><span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="n">encoding</span><span class="p">):</span></span><a href="#l1077"></a>
<span id="l1078">    <span class="c"># escape attribute value</span></span><a href="#l1078"></a>
<span id="l1079">    <span class="k">try</span><span class="p">:</span></span><a href="#l1079"></a>
<span id="l1080">        <span class="k">if</span> <span class="s">&quot;&amp;&quot;</span> <span class="ow">in</span> <span class="n">text</span><span class="p">:</span></span><a href="#l1080"></a>
<span id="l1081">            <span class="n">text</span> <span class="o">=</span> <span class="n">text</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&quot;&amp;&quot;</span><span class="p">,</span> <span class="s">&quot;&amp;amp;&quot;</span><span class="p">)</span></span><a href="#l1081"></a>
<span id="l1082">        <span class="k">if</span> <span class="s">&quot;&lt;&quot;</span> <span class="ow">in</span> <span class="n">text</span><span class="p">:</span></span><a href="#l1082"></a>
<span id="l1083">            <span class="n">text</span> <span class="o">=</span> <span class="n">text</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&quot;&lt;&quot;</span><span class="p">,</span> <span class="s">&quot;&amp;lt;&quot;</span><span class="p">)</span></span><a href="#l1083"></a>
<span id="l1084">        <span class="k">if</span> <span class="s">&quot;&gt;&quot;</span> <span class="ow">in</span> <span class="n">text</span><span class="p">:</span></span><a href="#l1084"></a>
<span id="l1085">            <span class="n">text</span> <span class="o">=</span> <span class="n">text</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&quot;&gt;&quot;</span><span class="p">,</span> <span class="s">&quot;&amp;gt;&quot;</span><span class="p">)</span></span><a href="#l1085"></a>
<span id="l1086">        <span class="k">if</span> <span class="s">&quot;</span><span class="se">\&quot;</span><span class="s">&quot;</span> <span class="ow">in</span> <span class="n">text</span><span class="p">:</span></span><a href="#l1086"></a>
<span id="l1087">            <span class="n">text</span> <span class="o">=</span> <span class="n">text</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&quot;</span><span class="se">\&quot;</span><span class="s">&quot;</span><span class="p">,</span> <span class="s">&quot;&amp;quot;&quot;</span><span class="p">)</span></span><a href="#l1087"></a>
<span id="l1088">        <span class="k">if</span> <span class="s">&quot;</span><span class="se">\n</span><span class="s">&quot;</span> <span class="ow">in</span> <span class="n">text</span><span class="p">:</span></span><a href="#l1088"></a>
<span id="l1089">            <span class="n">text</span> <span class="o">=</span> <span class="n">text</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&quot;</span><span class="se">\n</span><span class="s">&quot;</span><span class="p">,</span> <span class="s">&quot;&amp;#10;&quot;</span><span class="p">)</span></span><a href="#l1089"></a>
<span id="l1090">        <span class="k">return</span> <span class="n">text</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="n">encoding</span><span class="p">,</span> <span class="s">&quot;xmlcharrefreplace&quot;</span><span class="p">)</span></span><a href="#l1090"></a>
<span id="l1091">    <span class="k">except</span> <span class="p">(</span><span class="ne">TypeError</span><span class="p">,</span> <span class="ne">AttributeError</span><span class="p">):</span></span><a href="#l1091"></a>
<span id="l1092">        <span class="n">_raise_serialization_error</span><span class="p">(</span><span class="n">text</span><span class="p">)</span></span><a href="#l1092"></a>
<span id="l1093"></span><a href="#l1093"></a>
<span id="l1094"><span class="k">def</span> <span class="nf">_escape_attrib_html</span><span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="n">encoding</span><span class="p">):</span></span><a href="#l1094"></a>
<span id="l1095">    <span class="c"># escape attribute value</span></span><a href="#l1095"></a>
<span id="l1096">    <span class="k">try</span><span class="p">:</span></span><a href="#l1096"></a>
<span id="l1097">        <span class="k">if</span> <span class="s">&quot;&amp;&quot;</span> <span class="ow">in</span> <span class="n">text</span><span class="p">:</span></span><a href="#l1097"></a>
<span id="l1098">            <span class="n">text</span> <span class="o">=</span> <span class="n">text</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&quot;&amp;&quot;</span><span class="p">,</span> <span class="s">&quot;&amp;amp;&quot;</span><span class="p">)</span></span><a href="#l1098"></a>
<span id="l1099">        <span class="k">if</span> <span class="s">&quot;&gt;&quot;</span> <span class="ow">in</span> <span class="n">text</span><span class="p">:</span></span><a href="#l1099"></a>
<span id="l1100">            <span class="n">text</span> <span class="o">=</span> <span class="n">text</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&quot;&gt;&quot;</span><span class="p">,</span> <span class="s">&quot;&amp;gt;&quot;</span><span class="p">)</span></span><a href="#l1100"></a>
<span id="l1101">        <span class="k">if</span> <span class="s">&quot;</span><span class="se">\&quot;</span><span class="s">&quot;</span> <span class="ow">in</span> <span class="n">text</span><span class="p">:</span></span><a href="#l1101"></a>
<span id="l1102">            <span class="n">text</span> <span class="o">=</span> <span class="n">text</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&quot;</span><span class="se">\&quot;</span><span class="s">&quot;</span><span class="p">,</span> <span class="s">&quot;&amp;quot;&quot;</span><span class="p">)</span></span><a href="#l1102"></a>
<span id="l1103">        <span class="k">return</span> <span class="n">text</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="n">encoding</span><span class="p">,</span> <span class="s">&quot;xmlcharrefreplace&quot;</span><span class="p">)</span></span><a href="#l1103"></a>
<span id="l1104">    <span class="k">except</span> <span class="p">(</span><span class="ne">TypeError</span><span class="p">,</span> <span class="ne">AttributeError</span><span class="p">):</span></span><a href="#l1104"></a>
<span id="l1105">        <span class="n">_raise_serialization_error</span><span class="p">(</span><span class="n">text</span><span class="p">)</span></span><a href="#l1105"></a>
<span id="l1106"></span><a href="#l1106"></a>
<span id="l1107"><span class="c"># --------------------------------------------------------------------</span></span><a href="#l1107"></a>
<span id="l1108"></span><a href="#l1108"></a>
<span id="l1109"><span class="c">##</span></span><a href="#l1109"></a>
<span id="l1110"><span class="c"># Generates a string representation of an XML element, including all</span></span><a href="#l1110"></a>
<span id="l1111"><span class="c"># subelements.</span></span><a href="#l1111"></a>
<span id="l1112"><span class="c">#</span></span><a href="#l1112"></a>
<span id="l1113"><span class="c"># @param element An Element instance.</span></span><a href="#l1113"></a>
<span id="l1114"><span class="c"># @keyparam encoding Optional output encoding (default is US-ASCII).</span></span><a href="#l1114"></a>
<span id="l1115"><span class="c"># @keyparam method Optional output method (&quot;xml&quot;, &quot;html&quot;, &quot;text&quot; or</span></span><a href="#l1115"></a>
<span id="l1116"><span class="c">#     &quot;c14n&quot;; default is &quot;xml&quot;).</span></span><a href="#l1116"></a>
<span id="l1117"><span class="c"># @return An encoded string containing the XML data.</span></span><a href="#l1117"></a>
<span id="l1118"><span class="c"># @defreturn string</span></span><a href="#l1118"></a>
<span id="l1119"></span><a href="#l1119"></a>
<span id="l1120"><span class="k">def</span> <span class="nf">tostring</span><span class="p">(</span><span class="n">element</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">method</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l1120"></a>
<span id="l1121">    <span class="k">class</span> <span class="nc">dummy</span><span class="p">:</span></span><a href="#l1121"></a>
<span id="l1122">        <span class="k">pass</span></span><a href="#l1122"></a>
<span id="l1123">    <span class="n">data</span> <span class="o">=</span> <span class="p">[]</span></span><a href="#l1123"></a>
<span id="l1124">    <span class="nb">file</span> <span class="o">=</span> <span class="n">dummy</span><span class="p">()</span></span><a href="#l1124"></a>
<span id="l1125">    <span class="nb">file</span><span class="o">.</span><span class="n">write</span> <span class="o">=</span> <span class="n">data</span><span class="o">.</span><span class="n">append</span></span><a href="#l1125"></a>
<span id="l1126">    <span class="n">ElementTree</span><span class="p">(</span><span class="n">element</span><span class="p">)</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="nb">file</span><span class="p">,</span> <span class="n">encoding</span><span class="p">,</span> <span class="n">method</span><span class="o">=</span><span class="n">method</span><span class="p">)</span></span><a href="#l1126"></a>
<span id="l1127">    <span class="k">return</span> <span class="s">&quot;&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">data</span><span class="p">)</span></span><a href="#l1127"></a>
<span id="l1128"></span><a href="#l1128"></a>
<span id="l1129"><span class="c">##</span></span><a href="#l1129"></a>
<span id="l1130"><span class="c"># Generates a string representation of an XML element, including all</span></span><a href="#l1130"></a>
<span id="l1131"><span class="c"># subelements.  The string is returned as a sequence of string fragments.</span></span><a href="#l1131"></a>
<span id="l1132"><span class="c">#</span></span><a href="#l1132"></a>
<span id="l1133"><span class="c"># @param element An Element instance.</span></span><a href="#l1133"></a>
<span id="l1134"><span class="c"># @keyparam encoding Optional output encoding (default is US-ASCII).</span></span><a href="#l1134"></a>
<span id="l1135"><span class="c"># @keyparam method Optional output method (&quot;xml&quot;, &quot;html&quot;, &quot;text&quot; or</span></span><a href="#l1135"></a>
<span id="l1136"><span class="c">#     &quot;c14n&quot;; default is &quot;xml&quot;).</span></span><a href="#l1136"></a>
<span id="l1137"><span class="c"># @return A sequence object containing the XML data.</span></span><a href="#l1137"></a>
<span id="l1138"><span class="c"># @defreturn sequence</span></span><a href="#l1138"></a>
<span id="l1139"><span class="c"># @since 1.3</span></span><a href="#l1139"></a>
<span id="l1140"></span><a href="#l1140"></a>
<span id="l1141"><span class="k">def</span> <span class="nf">tostringlist</span><span class="p">(</span><span class="n">element</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">method</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l1141"></a>
<span id="l1142">    <span class="k">class</span> <span class="nc">dummy</span><span class="p">:</span></span><a href="#l1142"></a>
<span id="l1143">        <span class="k">pass</span></span><a href="#l1143"></a>
<span id="l1144">    <span class="n">data</span> <span class="o">=</span> <span class="p">[]</span></span><a href="#l1144"></a>
<span id="l1145">    <span class="nb">file</span> <span class="o">=</span> <span class="n">dummy</span><span class="p">()</span></span><a href="#l1145"></a>
<span id="l1146">    <span class="nb">file</span><span class="o">.</span><span class="n">write</span> <span class="o">=</span> <span class="n">data</span><span class="o">.</span><span class="n">append</span></span><a href="#l1146"></a>
<span id="l1147">    <span class="n">ElementTree</span><span class="p">(</span><span class="n">element</span><span class="p">)</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="nb">file</span><span class="p">,</span> <span class="n">encoding</span><span class="p">,</span> <span class="n">method</span><span class="o">=</span><span class="n">method</span><span class="p">)</span></span><a href="#l1147"></a>
<span id="l1148">    <span class="c"># FIXME: merge small fragments into larger parts</span></span><a href="#l1148"></a>
<span id="l1149">    <span class="k">return</span> <span class="n">data</span></span><a href="#l1149"></a>
<span id="l1150"></span><a href="#l1150"></a>
<span id="l1151"><span class="c">##</span></span><a href="#l1151"></a>
<span id="l1152"><span class="c"># Writes an element tree or element structure to sys.stdout.  This</span></span><a href="#l1152"></a>
<span id="l1153"><span class="c"># function should be used for debugging only.</span></span><a href="#l1153"></a>
<span id="l1154"><span class="c"># &lt;p&gt;</span></span><a href="#l1154"></a>
<span id="l1155"><span class="c"># The exact output format is implementation dependent.  In this</span></span><a href="#l1155"></a>
<span id="l1156"><span class="c"># version, it&#39;s written as an ordinary XML file.</span></span><a href="#l1156"></a>
<span id="l1157"><span class="c">#</span></span><a href="#l1157"></a>
<span id="l1158"><span class="c"># @param elem An element tree or an individual element.</span></span><a href="#l1158"></a>
<span id="l1159"></span><a href="#l1159"></a>
<span id="l1160"><span class="k">def</span> <span class="nf">dump</span><span class="p">(</span><span class="n">elem</span><span class="p">):</span></span><a href="#l1160"></a>
<span id="l1161">    <span class="c"># debugging</span></span><a href="#l1161"></a>
<span id="l1162">    <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">elem</span><span class="p">,</span> <span class="n">ElementTree</span><span class="p">):</span></span><a href="#l1162"></a>
<span id="l1163">        <span class="n">elem</span> <span class="o">=</span> <span class="n">ElementTree</span><span class="p">(</span><span class="n">elem</span><span class="p">)</span></span><a href="#l1163"></a>
<span id="l1164">    <span class="n">elem</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="p">)</span></span><a href="#l1164"></a>
<span id="l1165">    <span class="n">tail</span> <span class="o">=</span> <span class="n">elem</span><span class="o">.</span><span class="n">getroot</span><span class="p">()</span><span class="o">.</span><span class="n">tail</span></span><a href="#l1165"></a>
<span id="l1166">    <span class="k">if</span> <span class="ow">not</span> <span class="n">tail</span> <span class="ow">or</span> <span class="n">tail</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span> <span class="o">!=</span> <span class="s">&quot;</span><span class="se">\n</span><span class="s">&quot;</span><span class="p">:</span></span><a href="#l1166"></a>
<span id="l1167">        <span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&quot;</span><span class="se">\n</span><span class="s">&quot;</span><span class="p">)</span></span><a href="#l1167"></a>
<span id="l1168"></span><a href="#l1168"></a>
<span id="l1169"><span class="c"># --------------------------------------------------------------------</span></span><a href="#l1169"></a>
<span id="l1170"><span class="c"># parsing</span></span><a href="#l1170"></a>
<span id="l1171"></span><a href="#l1171"></a>
<span id="l1172"><span class="c">##</span></span><a href="#l1172"></a>
<span id="l1173"><span class="c"># Parses an XML document into an element tree.</span></span><a href="#l1173"></a>
<span id="l1174"><span class="c">#</span></span><a href="#l1174"></a>
<span id="l1175"><span class="c"># @param source A filename or file object containing XML data.</span></span><a href="#l1175"></a>
<span id="l1176"><span class="c"># @param parser An optional parser instance.  If not given, the</span></span><a href="#l1176"></a>
<span id="l1177"><span class="c">#     standard {@link XMLParser} parser is used.</span></span><a href="#l1177"></a>
<span id="l1178"><span class="c"># @return An ElementTree instance</span></span><a href="#l1178"></a>
<span id="l1179"></span><a href="#l1179"></a>
<span id="l1180"><span class="k">def</span> <span class="nf">parse</span><span class="p">(</span><span class="n">source</span><span class="p">,</span> <span class="n">parser</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l1180"></a>
<span id="l1181">    <span class="n">tree</span> <span class="o">=</span> <span class="n">ElementTree</span><span class="p">()</span></span><a href="#l1181"></a>
<span id="l1182">    <span class="n">tree</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">source</span><span class="p">,</span> <span class="n">parser</span><span class="p">)</span></span><a href="#l1182"></a>
<span id="l1183">    <span class="k">return</span> <span class="n">tree</span></span><a href="#l1183"></a>
<span id="l1184"></span><a href="#l1184"></a>
<span id="l1185"><span class="c">##</span></span><a href="#l1185"></a>
<span id="l1186"><span class="c"># Parses an XML document into an element tree incrementally, and reports</span></span><a href="#l1186"></a>
<span id="l1187"><span class="c"># what&#39;s going on to the user.</span></span><a href="#l1187"></a>
<span id="l1188"><span class="c">#</span></span><a href="#l1188"></a>
<span id="l1189"><span class="c"># @param source A filename or file object containing XML data.</span></span><a href="#l1189"></a>
<span id="l1190"><span class="c"># @param events A list of events to report back.  If omitted, only &quot;end&quot;</span></span><a href="#l1190"></a>
<span id="l1191"><span class="c">#     events are reported.</span></span><a href="#l1191"></a>
<span id="l1192"><span class="c"># @param parser An optional parser instance.  If not given, the</span></span><a href="#l1192"></a>
<span id="l1193"><span class="c">#     standard {@link XMLParser} parser is used.</span></span><a href="#l1193"></a>
<span id="l1194"><span class="c"># @return A (event, elem) iterator.</span></span><a href="#l1194"></a>
<span id="l1195"></span><a href="#l1195"></a>
<span id="l1196"><span class="k">def</span> <span class="nf">iterparse</span><span class="p">(</span><span class="n">source</span><span class="p">,</span> <span class="n">events</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">parser</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l1196"></a>
<span id="l1197">    <span class="n">close_source</span> <span class="o">=</span> <span class="bp">False</span></span><a href="#l1197"></a>
<span id="l1198">    <span class="k">if</span> <span class="ow">not</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">source</span><span class="p">,</span> <span class="s">&quot;read&quot;</span><span class="p">):</span></span><a href="#l1198"></a>
<span id="l1199">        <span class="n">source</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">source</span><span class="p">,</span> <span class="s">&quot;rb&quot;</span><span class="p">)</span></span><a href="#l1199"></a>
<span id="l1200">        <span class="n">close_source</span> <span class="o">=</span> <span class="bp">True</span></span><a href="#l1200"></a>
<span id="l1201">    <span class="k">if</span> <span class="ow">not</span> <span class="n">parser</span><span class="p">:</span></span><a href="#l1201"></a>
<span id="l1202">        <span class="n">parser</span> <span class="o">=</span> <span class="n">XMLParser</span><span class="p">(</span><span class="n">target</span><span class="o">=</span><span class="n">TreeBuilder</span><span class="p">())</span></span><a href="#l1202"></a>
<span id="l1203">    <span class="k">return</span> <span class="n">_IterParseIterator</span><span class="p">(</span><span class="n">source</span><span class="p">,</span> <span class="n">events</span><span class="p">,</span> <span class="n">parser</span><span class="p">,</span> <span class="n">close_source</span><span class="p">)</span></span><a href="#l1203"></a>
<span id="l1204"></span><a href="#l1204"></a>
<span id="l1205"><span class="k">class</span> <span class="nc">_IterParseIterator</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></span><a href="#l1205"></a>
<span id="l1206"></span><a href="#l1206"></a>
<span id="l1207">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">source</span><span class="p">,</span> <span class="n">events</span><span class="p">,</span> <span class="n">parser</span><span class="p">,</span> <span class="n">close_source</span><span class="o">=</span><span class="bp">False</span><span class="p">):</span></span><a href="#l1207"></a>
<span id="l1208">        <span class="bp">self</span><span class="o">.</span><span class="n">_file</span> <span class="o">=</span> <span class="n">source</span></span><a href="#l1208"></a>
<span id="l1209">        <span class="bp">self</span><span class="o">.</span><span class="n">_close_file</span> <span class="o">=</span> <span class="n">close_source</span></span><a href="#l1209"></a>
<span id="l1210">        <span class="bp">self</span><span class="o">.</span><span class="n">_events</span> <span class="o">=</span> <span class="p">[]</span></span><a href="#l1210"></a>
<span id="l1211">        <span class="bp">self</span><span class="o">.</span><span class="n">_index</span> <span class="o">=</span> <span class="mi">0</span></span><a href="#l1211"></a>
<span id="l1212">        <span class="bp">self</span><span class="o">.</span><span class="n">_error</span> <span class="o">=</span> <span class="bp">None</span></span><a href="#l1212"></a>
<span id="l1213">        <span class="bp">self</span><span class="o">.</span><span class="n">root</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_root</span> <span class="o">=</span> <span class="bp">None</span></span><a href="#l1213"></a>
<span id="l1214">        <span class="bp">self</span><span class="o">.</span><span class="n">_parser</span> <span class="o">=</span> <span class="n">parser</span></span><a href="#l1214"></a>
<span id="l1215">        <span class="c"># wire up the parser for event reporting</span></span><a href="#l1215"></a>
<span id="l1216">        <span class="n">parser</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser</span><span class="o">.</span><span class="n">_parser</span></span><a href="#l1216"></a>
<span id="l1217">        <span class="n">append</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_events</span><span class="o">.</span><span class="n">append</span></span><a href="#l1217"></a>
<span id="l1218">        <span class="k">if</span> <span class="n">events</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1218"></a>
<span id="l1219">            <span class="n">events</span> <span class="o">=</span> <span class="p">[</span><span class="s">&quot;end&quot;</span><span class="p">]</span></span><a href="#l1219"></a>
<span id="l1220">        <span class="k">for</span> <span class="n">event</span> <span class="ow">in</span> <span class="n">events</span><span class="p">:</span></span><a href="#l1220"></a>
<span id="l1221">            <span class="k">if</span> <span class="n">event</span> <span class="o">==</span> <span class="s">&quot;start&quot;</span><span class="p">:</span></span><a href="#l1221"></a>
<span id="l1222">                <span class="k">try</span><span class="p">:</span></span><a href="#l1222"></a>
<span id="l1223">                    <span class="n">parser</span><span class="o">.</span><span class="n">ordered_attributes</span> <span class="o">=</span> <span class="mi">1</span></span><a href="#l1223"></a>
<span id="l1224">                    <span class="n">parser</span><span class="o">.</span><span class="n">specified_attributes</span> <span class="o">=</span> <span class="mi">1</span></span><a href="#l1224"></a>
<span id="l1225">                    <span class="k">def</span> <span class="nf">handler</span><span class="p">(</span><span class="n">tag</span><span class="p">,</span> <span class="n">attrib_in</span><span class="p">,</span> <span class="n">event</span><span class="o">=</span><span class="n">event</span><span class="p">,</span> <span class="n">append</span><span class="o">=</span><span class="n">append</span><span class="p">,</span></span><a href="#l1225"></a>
<span id="l1226">                                <span class="n">start</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_parser</span><span class="o">.</span><span class="n">_start_list</span><span class="p">):</span></span><a href="#l1226"></a>
<span id="l1227">                        <span class="n">append</span><span class="p">((</span><span class="n">event</span><span class="p">,</span> <span class="n">start</span><span class="p">(</span><span class="n">tag</span><span class="p">,</span> <span class="n">attrib_in</span><span class="p">)))</span></span><a href="#l1227"></a>
<span id="l1228">                    <span class="n">parser</span><span class="o">.</span><span class="n">StartElementHandler</span> <span class="o">=</span> <span class="n">handler</span></span><a href="#l1228"></a>
<span id="l1229">                <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span></span><a href="#l1229"></a>
<span id="l1230">                    <span class="k">def</span> <span class="nf">handler</span><span class="p">(</span><span class="n">tag</span><span class="p">,</span> <span class="n">attrib_in</span><span class="p">,</span> <span class="n">event</span><span class="o">=</span><span class="n">event</span><span class="p">,</span> <span class="n">append</span><span class="o">=</span><span class="n">append</span><span class="p">,</span></span><a href="#l1230"></a>
<span id="l1231">                                <span class="n">start</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_parser</span><span class="o">.</span><span class="n">_start</span><span class="p">):</span></span><a href="#l1231"></a>
<span id="l1232">                        <span class="n">append</span><span class="p">((</span><span class="n">event</span><span class="p">,</span> <span class="n">start</span><span class="p">(</span><span class="n">tag</span><span class="p">,</span> <span class="n">attrib_in</span><span class="p">)))</span></span><a href="#l1232"></a>
<span id="l1233">                    <span class="n">parser</span><span class="o">.</span><span class="n">StartElementHandler</span> <span class="o">=</span> <span class="n">handler</span></span><a href="#l1233"></a>
<span id="l1234">            <span class="k">elif</span> <span class="n">event</span> <span class="o">==</span> <span class="s">&quot;end&quot;</span><span class="p">:</span></span><a href="#l1234"></a>
<span id="l1235">                <span class="k">def</span> <span class="nf">handler</span><span class="p">(</span><span class="n">tag</span><span class="p">,</span> <span class="n">event</span><span class="o">=</span><span class="n">event</span><span class="p">,</span> <span class="n">append</span><span class="o">=</span><span class="n">append</span><span class="p">,</span></span><a href="#l1235"></a>
<span id="l1236">                            <span class="n">end</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_parser</span><span class="o">.</span><span class="n">_end</span><span class="p">):</span></span><a href="#l1236"></a>
<span id="l1237">                    <span class="n">append</span><span class="p">((</span><span class="n">event</span><span class="p">,</span> <span class="n">end</span><span class="p">(</span><span class="n">tag</span><span class="p">)))</span></span><a href="#l1237"></a>
<span id="l1238">                <span class="n">parser</span><span class="o">.</span><span class="n">EndElementHandler</span> <span class="o">=</span> <span class="n">handler</span></span><a href="#l1238"></a>
<span id="l1239">            <span class="k">elif</span> <span class="n">event</span> <span class="o">==</span> <span class="s">&quot;start-ns&quot;</span><span class="p">:</span></span><a href="#l1239"></a>
<span id="l1240">                <span class="k">def</span> <span class="nf">handler</span><span class="p">(</span><span class="n">prefix</span><span class="p">,</span> <span class="n">uri</span><span class="p">,</span> <span class="n">event</span><span class="o">=</span><span class="n">event</span><span class="p">,</span> <span class="n">append</span><span class="o">=</span><span class="n">append</span><span class="p">):</span></span><a href="#l1240"></a>
<span id="l1241">                    <span class="k">try</span><span class="p">:</span></span><a href="#l1241"></a>
<span id="l1242">                        <span class="n">uri</span> <span class="o">=</span> <span class="p">(</span><span class="n">uri</span> <span class="ow">or</span> <span class="s">&quot;&quot;</span><span class="p">)</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="s">&quot;ascii&quot;</span><span class="p">)</span></span><a href="#l1242"></a>
<span id="l1243">                    <span class="k">except</span> <span class="ne">UnicodeError</span><span class="p">:</span></span><a href="#l1243"></a>
<span id="l1244">                        <span class="k">pass</span></span><a href="#l1244"></a>
<span id="l1245">                    <span class="n">append</span><span class="p">((</span><span class="n">event</span><span class="p">,</span> <span class="p">(</span><span class="n">prefix</span> <span class="ow">or</span> <span class="s">&quot;&quot;</span><span class="p">,</span> <span class="n">uri</span> <span class="ow">or</span> <span class="s">&quot;&quot;</span><span class="p">)))</span></span><a href="#l1245"></a>
<span id="l1246">                <span class="n">parser</span><span class="o">.</span><span class="n">StartNamespaceDeclHandler</span> <span class="o">=</span> <span class="n">handler</span></span><a href="#l1246"></a>
<span id="l1247">            <span class="k">elif</span> <span class="n">event</span> <span class="o">==</span> <span class="s">&quot;end-ns&quot;</span><span class="p">:</span></span><a href="#l1247"></a>
<span id="l1248">                <span class="k">def</span> <span class="nf">handler</span><span class="p">(</span><span class="n">prefix</span><span class="p">,</span> <span class="n">event</span><span class="o">=</span><span class="n">event</span><span class="p">,</span> <span class="n">append</span><span class="o">=</span><span class="n">append</span><span class="p">):</span></span><a href="#l1248"></a>
<span id="l1249">                    <span class="n">append</span><span class="p">((</span><span class="n">event</span><span class="p">,</span> <span class="bp">None</span><span class="p">))</span></span><a href="#l1249"></a>
<span id="l1250">                <span class="n">parser</span><span class="o">.</span><span class="n">EndNamespaceDeclHandler</span> <span class="o">=</span> <span class="n">handler</span></span><a href="#l1250"></a>
<span id="l1251">            <span class="k">else</span><span class="p">:</span></span><a href="#l1251"></a>
<span id="l1252">                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s">&quot;unknown event </span><span class="si">%r</span><span class="s">&quot;</span> <span class="o">%</span> <span class="n">event</span><span class="p">)</span></span><a href="#l1252"></a>
<span id="l1253"></span><a href="#l1253"></a>
<span id="l1254">    <span class="k">def</span> <span class="nf">next</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1254"></a>
<span id="l1255">        <span class="k">while</span> <span class="mi">1</span><span class="p">:</span></span><a href="#l1255"></a>
<span id="l1256">            <span class="k">try</span><span class="p">:</span></span><a href="#l1256"></a>
<span id="l1257">                <span class="n">item</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_events</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="p">]</span></span><a href="#l1257"></a>
<span id="l1258">                <span class="bp">self</span><span class="o">.</span><span class="n">_index</span> <span class="o">+=</span> <span class="mi">1</span></span><a href="#l1258"></a>
<span id="l1259">                <span class="k">return</span> <span class="n">item</span></span><a href="#l1259"></a>
<span id="l1260">            <span class="k">except</span> <span class="ne">IndexError</span><span class="p">:</span></span><a href="#l1260"></a>
<span id="l1261">                <span class="k">pass</span></span><a href="#l1261"></a>
<span id="l1262">            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_error</span><span class="p">:</span></span><a href="#l1262"></a>
<span id="l1263">                <span class="n">e</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_error</span></span><a href="#l1263"></a>
<span id="l1264">                <span class="bp">self</span><span class="o">.</span><span class="n">_error</span> <span class="o">=</span> <span class="bp">None</span></span><a href="#l1264"></a>
<span id="l1265">                <span class="k">raise</span> <span class="n">e</span></span><a href="#l1265"></a>
<span id="l1266">            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1266"></a>
<span id="l1267">                <span class="bp">self</span><span class="o">.</span><span class="n">root</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_root</span></span><a href="#l1267"></a>
<span id="l1268">                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_close_file</span><span class="p">:</span></span><a href="#l1268"></a>
<span id="l1269">                    <span class="bp">self</span><span class="o">.</span><span class="n">_file</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></span><a href="#l1269"></a>
<span id="l1270">                <span class="k">raise</span> <span class="ne">StopIteration</span></span><a href="#l1270"></a>
<span id="l1271">            <span class="c"># load event buffer</span></span><a href="#l1271"></a>
<span id="l1272">            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">_events</span><span class="p">[:]</span></span><a href="#l1272"></a>
<span id="l1273">            <span class="bp">self</span><span class="o">.</span><span class="n">_index</span> <span class="o">=</span> <span class="mi">0</span></span><a href="#l1273"></a>
<span id="l1274">            <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_file</span><span class="o">.</span><span class="n">read</span><span class="p">(</span><span class="mi">16384</span><span class="p">)</span></span><a href="#l1274"></a>
<span id="l1275">            <span class="k">if</span> <span class="n">data</span><span class="p">:</span></span><a href="#l1275"></a>
<span id="l1276">                <span class="k">try</span><span class="p">:</span></span><a href="#l1276"></a>
<span id="l1277">                    <span class="bp">self</span><span class="o">.</span><span class="n">_parser</span><span class="o">.</span><span class="n">feed</span><span class="p">(</span><span class="n">data</span><span class="p">)</span></span><a href="#l1277"></a>
<span id="l1278">                <span class="k">except</span> <span class="ne">SyntaxError</span> <span class="k">as</span> <span class="n">exc</span><span class="p">:</span></span><a href="#l1278"></a>
<span id="l1279">                    <span class="bp">self</span><span class="o">.</span><span class="n">_error</span> <span class="o">=</span> <span class="n">exc</span></span><a href="#l1279"></a>
<span id="l1280">            <span class="k">else</span><span class="p">:</span></span><a href="#l1280"></a>
<span id="l1281">                <span class="bp">self</span><span class="o">.</span><span class="n">_root</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></span><a href="#l1281"></a>
<span id="l1282">                <span class="bp">self</span><span class="o">.</span><span class="n">_parser</span> <span class="o">=</span> <span class="bp">None</span></span><a href="#l1282"></a>
<span id="l1283"></span><a href="#l1283"></a>
<span id="l1284">    <span class="k">def</span> <span class="nf">__iter__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1284"></a>
<span id="l1285">        <span class="k">return</span> <span class="bp">self</span></span><a href="#l1285"></a>
<span id="l1286"></span><a href="#l1286"></a>
<span id="l1287"><span class="c">##</span></span><a href="#l1287"></a>
<span id="l1288"><span class="c"># Parses an XML document from a string constant.  This function can</span></span><a href="#l1288"></a>
<span id="l1289"><span class="c"># be used to embed &quot;XML literals&quot; in Python code.</span></span><a href="#l1289"></a>
<span id="l1290"><span class="c">#</span></span><a href="#l1290"></a>
<span id="l1291"><span class="c"># @param source A string containing XML data.</span></span><a href="#l1291"></a>
<span id="l1292"><span class="c"># @param parser An optional parser instance.  If not given, the</span></span><a href="#l1292"></a>
<span id="l1293"><span class="c">#     standard {@link XMLParser} parser is used.</span></span><a href="#l1293"></a>
<span id="l1294"><span class="c"># @return An Element instance.</span></span><a href="#l1294"></a>
<span id="l1295"><span class="c"># @defreturn Element</span></span><a href="#l1295"></a>
<span id="l1296"></span><a href="#l1296"></a>
<span id="l1297"><span class="k">def</span> <span class="nf">XML</span><span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="n">parser</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l1297"></a>
<span id="l1298">    <span class="k">if</span> <span class="ow">not</span> <span class="n">parser</span><span class="p">:</span></span><a href="#l1298"></a>
<span id="l1299">        <span class="n">parser</span> <span class="o">=</span> <span class="n">XMLParser</span><span class="p">(</span><span class="n">target</span><span class="o">=</span><span class="n">TreeBuilder</span><span class="p">())</span></span><a href="#l1299"></a>
<span id="l1300">    <span class="n">parser</span><span class="o">.</span><span class="n">feed</span><span class="p">(</span><span class="n">text</span><span class="p">)</span></span><a href="#l1300"></a>
<span id="l1301">    <span class="k">return</span> <span class="n">parser</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></span><a href="#l1301"></a>
<span id="l1302"></span><a href="#l1302"></a>
<span id="l1303"><span class="c">##</span></span><a href="#l1303"></a>
<span id="l1304"><span class="c"># Parses an XML document from a string constant, and also returns</span></span><a href="#l1304"></a>
<span id="l1305"><span class="c"># a dictionary which maps from element id:s to elements.</span></span><a href="#l1305"></a>
<span id="l1306"><span class="c">#</span></span><a href="#l1306"></a>
<span id="l1307"><span class="c"># @param source A string containing XML data.</span></span><a href="#l1307"></a>
<span id="l1308"><span class="c"># @param parser An optional parser instance.  If not given, the</span></span><a href="#l1308"></a>
<span id="l1309"><span class="c">#     standard {@link XMLParser} parser is used.</span></span><a href="#l1309"></a>
<span id="l1310"><span class="c"># @return A tuple containing an Element instance and a dictionary.</span></span><a href="#l1310"></a>
<span id="l1311"><span class="c"># @defreturn (Element, dictionary)</span></span><a href="#l1311"></a>
<span id="l1312"></span><a href="#l1312"></a>
<span id="l1313"><span class="k">def</span> <span class="nf">XMLID</span><span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="n">parser</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l1313"></a>
<span id="l1314">    <span class="k">if</span> <span class="ow">not</span> <span class="n">parser</span><span class="p">:</span></span><a href="#l1314"></a>
<span id="l1315">        <span class="n">parser</span> <span class="o">=</span> <span class="n">XMLParser</span><span class="p">(</span><span class="n">target</span><span class="o">=</span><span class="n">TreeBuilder</span><span class="p">())</span></span><a href="#l1315"></a>
<span id="l1316">    <span class="n">parser</span><span class="o">.</span><span class="n">feed</span><span class="p">(</span><span class="n">text</span><span class="p">)</span></span><a href="#l1316"></a>
<span id="l1317">    <span class="n">tree</span> <span class="o">=</span> <span class="n">parser</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></span><a href="#l1317"></a>
<span id="l1318">    <span class="n">ids</span> <span class="o">=</span> <span class="p">{}</span></span><a href="#l1318"></a>
<span id="l1319">    <span class="k">for</span> <span class="n">elem</span> <span class="ow">in</span> <span class="n">tree</span><span class="o">.</span><span class="n">iter</span><span class="p">():</span></span><a href="#l1319"></a>
<span id="l1320">        <span class="nb">id</span> <span class="o">=</span> <span class="n">elem</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&quot;id&quot;</span><span class="p">)</span></span><a href="#l1320"></a>
<span id="l1321">        <span class="k">if</span> <span class="nb">id</span><span class="p">:</span></span><a href="#l1321"></a>
<span id="l1322">            <span class="n">ids</span><span class="p">[</span><span class="nb">id</span><span class="p">]</span> <span class="o">=</span> <span class="n">elem</span></span><a href="#l1322"></a>
<span id="l1323">    <span class="k">return</span> <span class="n">tree</span><span class="p">,</span> <span class="n">ids</span></span><a href="#l1323"></a>
<span id="l1324"></span><a href="#l1324"></a>
<span id="l1325"><span class="c">##</span></span><a href="#l1325"></a>
<span id="l1326"><span class="c"># Parses an XML document from a string constant.  Same as {@link #XML}.</span></span><a href="#l1326"></a>
<span id="l1327"><span class="c">#</span></span><a href="#l1327"></a>
<span id="l1328"><span class="c"># @def fromstring(text)</span></span><a href="#l1328"></a>
<span id="l1329"><span class="c"># @param source A string containing XML data.</span></span><a href="#l1329"></a>
<span id="l1330"><span class="c"># @return An Element instance.</span></span><a href="#l1330"></a>
<span id="l1331"><span class="c"># @defreturn Element</span></span><a href="#l1331"></a>
<span id="l1332"></span><a href="#l1332"></a>
<span id="l1333"><span class="n">fromstring</span> <span class="o">=</span> <span class="n">XML</span></span><a href="#l1333"></a>
<span id="l1334"></span><a href="#l1334"></a>
<span id="l1335"><span class="c">##</span></span><a href="#l1335"></a>
<span id="l1336"><span class="c"># Parses an XML document from a sequence of string fragments.</span></span><a href="#l1336"></a>
<span id="l1337"><span class="c">#</span></span><a href="#l1337"></a>
<span id="l1338"><span class="c"># @param sequence A list or other sequence containing XML data fragments.</span></span><a href="#l1338"></a>
<span id="l1339"><span class="c"># @param parser An optional parser instance.  If not given, the</span></span><a href="#l1339"></a>
<span id="l1340"><span class="c">#     standard {@link XMLParser} parser is used.</span></span><a href="#l1340"></a>
<span id="l1341"><span class="c"># @return An Element instance.</span></span><a href="#l1341"></a>
<span id="l1342"><span class="c"># @defreturn Element</span></span><a href="#l1342"></a>
<span id="l1343"><span class="c"># @since 1.3</span></span><a href="#l1343"></a>
<span id="l1344"></span><a href="#l1344"></a>
<span id="l1345"><span class="k">def</span> <span class="nf">fromstringlist</span><span class="p">(</span><span class="n">sequence</span><span class="p">,</span> <span class="n">parser</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l1345"></a>
<span id="l1346">    <span class="k">if</span> <span class="ow">not</span> <span class="n">parser</span><span class="p">:</span></span><a href="#l1346"></a>
<span id="l1347">        <span class="n">parser</span> <span class="o">=</span> <span class="n">XMLParser</span><span class="p">(</span><span class="n">target</span><span class="o">=</span><span class="n">TreeBuilder</span><span class="p">())</span></span><a href="#l1347"></a>
<span id="l1348">    <span class="k">for</span> <span class="n">text</span> <span class="ow">in</span> <span class="n">sequence</span><span class="p">:</span></span><a href="#l1348"></a>
<span id="l1349">        <span class="n">parser</span><span class="o">.</span><span class="n">feed</span><span class="p">(</span><span class="n">text</span><span class="p">)</span></span><a href="#l1349"></a>
<span id="l1350">    <span class="k">return</span> <span class="n">parser</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></span><a href="#l1350"></a>
<span id="l1351"></span><a href="#l1351"></a>
<span id="l1352"><span class="c"># --------------------------------------------------------------------</span></span><a href="#l1352"></a>
<span id="l1353"></span><a href="#l1353"></a>
<span id="l1354"><span class="c">##</span></span><a href="#l1354"></a>
<span id="l1355"><span class="c"># Generic element structure builder.  This builder converts a sequence</span></span><a href="#l1355"></a>
<span id="l1356"><span class="c"># of {@link #TreeBuilder.start}, {@link #TreeBuilder.data}, and {@link</span></span><a href="#l1356"></a>
<span id="l1357"><span class="c"># #TreeBuilder.end} method calls to a well-formed element structure.</span></span><a href="#l1357"></a>
<span id="l1358"><span class="c"># &lt;p&gt;</span></span><a href="#l1358"></a>
<span id="l1359"><span class="c"># You can use this class to build an element structure using a custom XML</span></span><a href="#l1359"></a>
<span id="l1360"><span class="c"># parser, or a parser for some other XML-like format.</span></span><a href="#l1360"></a>
<span id="l1361"><span class="c">#</span></span><a href="#l1361"></a>
<span id="l1362"><span class="c"># @param element_factory Optional element factory.  This factory</span></span><a href="#l1362"></a>
<span id="l1363"><span class="c">#    is called to create new Element instances, as necessary.</span></span><a href="#l1363"></a>
<span id="l1364"></span><a href="#l1364"></a>
<span id="l1365"><span class="k">class</span> <span class="nc">TreeBuilder</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></span><a href="#l1365"></a>
<span id="l1366"></span><a href="#l1366"></a>
<span id="l1367">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">element_factory</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l1367"></a>
<span id="l1368">        <span class="bp">self</span><span class="o">.</span><span class="n">_data</span> <span class="o">=</span> <span class="p">[]</span> <span class="c"># data collector</span></span><a href="#l1368"></a>
<span id="l1369">        <span class="bp">self</span><span class="o">.</span><span class="n">_elem</span> <span class="o">=</span> <span class="p">[]</span> <span class="c"># element stack</span></span><a href="#l1369"></a>
<span id="l1370">        <span class="bp">self</span><span class="o">.</span><span class="n">_last</span> <span class="o">=</span> <span class="bp">None</span> <span class="c"># last element</span></span><a href="#l1370"></a>
<span id="l1371">        <span class="bp">self</span><span class="o">.</span><span class="n">_tail</span> <span class="o">=</span> <span class="bp">None</span> <span class="c"># true if we&#39;re after an end tag</span></span><a href="#l1371"></a>
<span id="l1372">        <span class="k">if</span> <span class="n">element_factory</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1372"></a>
<span id="l1373">            <span class="n">element_factory</span> <span class="o">=</span> <span class="n">Element</span></span><a href="#l1373"></a>
<span id="l1374">        <span class="bp">self</span><span class="o">.</span><span class="n">_factory</span> <span class="o">=</span> <span class="n">element_factory</span></span><a href="#l1374"></a>
<span id="l1375"></span><a href="#l1375"></a>
<span id="l1376">    <span class="c">##</span></span><a href="#l1376"></a>
<span id="l1377">    <span class="c"># Flushes the builder buffers, and returns the toplevel document</span></span><a href="#l1377"></a>
<span id="l1378">    <span class="c"># element.</span></span><a href="#l1378"></a>
<span id="l1379">    <span class="c">#</span></span><a href="#l1379"></a>
<span id="l1380">    <span class="c"># @return An Element instance.</span></span><a href="#l1380"></a>
<span id="l1381">    <span class="c"># @defreturn Element</span></span><a href="#l1381"></a>
<span id="l1382"></span><a href="#l1382"></a>
<span id="l1383">    <span class="k">def</span> <span class="nf">close</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1383"></a>
<span id="l1384">        <span class="k">assert</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_elem</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span><span class="p">,</span> <span class="s">&quot;missing end tags&quot;</span></span><a href="#l1384"></a>
<span id="l1385">        <span class="k">assert</span> <span class="bp">self</span><span class="o">.</span><span class="n">_last</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">,</span> <span class="s">&quot;missing toplevel element&quot;</span></span><a href="#l1385"></a>
<span id="l1386">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_last</span></span><a href="#l1386"></a>
<span id="l1387"></span><a href="#l1387"></a>
<span id="l1388">    <span class="k">def</span> <span class="nf">_flush</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1388"></a>
<span id="l1389">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_data</span><span class="p">:</span></span><a href="#l1389"></a>
<span id="l1390">            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_last</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1390"></a>
<span id="l1391">                <span class="n">text</span> <span class="o">=</span> <span class="s">&quot;&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_data</span><span class="p">)</span></span><a href="#l1391"></a>
<span id="l1392">                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tail</span><span class="p">:</span></span><a href="#l1392"></a>
<span id="l1393">                    <span class="k">assert</span> <span class="bp">self</span><span class="o">.</span><span class="n">_last</span><span class="o">.</span><span class="n">tail</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">,</span> <span class="s">&quot;internal error (tail)&quot;</span></span><a href="#l1393"></a>
<span id="l1394">                    <span class="bp">self</span><span class="o">.</span><span class="n">_last</span><span class="o">.</span><span class="n">tail</span> <span class="o">=</span> <span class="n">text</span></span><a href="#l1394"></a>
<span id="l1395">                <span class="k">else</span><span class="p">:</span></span><a href="#l1395"></a>
<span id="l1396">                    <span class="k">assert</span> <span class="bp">self</span><span class="o">.</span><span class="n">_last</span><span class="o">.</span><span class="n">text</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">,</span> <span class="s">&quot;internal error (text)&quot;</span></span><a href="#l1396"></a>
<span id="l1397">                    <span class="bp">self</span><span class="o">.</span><span class="n">_last</span><span class="o">.</span><span class="n">text</span> <span class="o">=</span> <span class="n">text</span></span><a href="#l1397"></a>
<span id="l1398">            <span class="bp">self</span><span class="o">.</span><span class="n">_data</span> <span class="o">=</span> <span class="p">[]</span></span><a href="#l1398"></a>
<span id="l1399"></span><a href="#l1399"></a>
<span id="l1400">    <span class="c">##</span></span><a href="#l1400"></a>
<span id="l1401">    <span class="c"># Adds text to the current element.</span></span><a href="#l1401"></a>
<span id="l1402">    <span class="c">#</span></span><a href="#l1402"></a>
<span id="l1403">    <span class="c"># @param data A string.  This should be either an 8-bit string</span></span><a href="#l1403"></a>
<span id="l1404">    <span class="c">#    containing ASCII text, or a Unicode string.</span></span><a href="#l1404"></a>
<span id="l1405"></span><a href="#l1405"></a>
<span id="l1406">    <span class="k">def</span> <span class="nf">data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span></span><a href="#l1406"></a>
<span id="l1407">        <span class="bp">self</span><span class="o">.</span><span class="n">_data</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">data</span><span class="p">)</span></span><a href="#l1407"></a>
<span id="l1408"></span><a href="#l1408"></a>
<span id="l1409">    <span class="c">##</span></span><a href="#l1409"></a>
<span id="l1410">    <span class="c"># Opens a new element.</span></span><a href="#l1410"></a>
<span id="l1411">    <span class="c">#</span></span><a href="#l1411"></a>
<span id="l1412">    <span class="c"># @param tag The element name.</span></span><a href="#l1412"></a>
<span id="l1413">    <span class="c"># @param attrib A dictionary containing element attributes.</span></span><a href="#l1413"></a>
<span id="l1414">    <span class="c"># @return The opened element.</span></span><a href="#l1414"></a>
<span id="l1415">    <span class="c"># @defreturn Element</span></span><a href="#l1415"></a>
<span id="l1416"></span><a href="#l1416"></a>
<span id="l1417">    <span class="k">def</span> <span class="nf">start</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tag</span><span class="p">,</span> <span class="n">attrs</span><span class="p">):</span></span><a href="#l1417"></a>
<span id="l1418">        <span class="bp">self</span><span class="o">.</span><span class="n">_flush</span><span class="p">()</span></span><a href="#l1418"></a>
<span id="l1419">        <span class="bp">self</span><span class="o">.</span><span class="n">_last</span> <span class="o">=</span> <span class="n">elem</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_factory</span><span class="p">(</span><span class="n">tag</span><span class="p">,</span> <span class="n">attrs</span><span class="p">)</span></span><a href="#l1419"></a>
<span id="l1420">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_elem</span><span class="p">:</span></span><a href="#l1420"></a>
<span id="l1421">            <span class="bp">self</span><span class="o">.</span><span class="n">_elem</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">elem</span><span class="p">)</span></span><a href="#l1421"></a>
<span id="l1422">        <span class="bp">self</span><span class="o">.</span><span class="n">_elem</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">elem</span><span class="p">)</span></span><a href="#l1422"></a>
<span id="l1423">        <span class="bp">self</span><span class="o">.</span><span class="n">_tail</span> <span class="o">=</span> <span class="mi">0</span></span><a href="#l1423"></a>
<span id="l1424">        <span class="k">return</span> <span class="n">elem</span></span><a href="#l1424"></a>
<span id="l1425"></span><a href="#l1425"></a>
<span id="l1426">    <span class="c">##</span></span><a href="#l1426"></a>
<span id="l1427">    <span class="c"># Closes the current element.</span></span><a href="#l1427"></a>
<span id="l1428">    <span class="c">#</span></span><a href="#l1428"></a>
<span id="l1429">    <span class="c"># @param tag The element name.</span></span><a href="#l1429"></a>
<span id="l1430">    <span class="c"># @return The closed element.</span></span><a href="#l1430"></a>
<span id="l1431">    <span class="c"># @defreturn Element</span></span><a href="#l1431"></a>
<span id="l1432"></span><a href="#l1432"></a>
<span id="l1433">    <span class="k">def</span> <span class="nf">end</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tag</span><span class="p">):</span></span><a href="#l1433"></a>
<span id="l1434">        <span class="bp">self</span><span class="o">.</span><span class="n">_flush</span><span class="p">()</span></span><a href="#l1434"></a>
<span id="l1435">        <span class="bp">self</span><span class="o">.</span><span class="n">_last</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_elem</span><span class="o">.</span><span class="n">pop</span><span class="p">()</span></span><a href="#l1435"></a>
<span id="l1436">        <span class="k">assert</span> <span class="bp">self</span><span class="o">.</span><span class="n">_last</span><span class="o">.</span><span class="n">tag</span> <span class="o">==</span> <span class="n">tag</span><span class="p">,</span>\</span><a href="#l1436"></a>
<span id="l1437">               <span class="s">&quot;end tag mismatch (expected </span><span class="si">%s</span><span class="s">, got </span><span class="si">%s</span><span class="s">)&quot;</span> <span class="o">%</span> <span class="p">(</span></span><a href="#l1437"></a>
<span id="l1438">                   <span class="bp">self</span><span class="o">.</span><span class="n">_last</span><span class="o">.</span><span class="n">tag</span><span class="p">,</span> <span class="n">tag</span><span class="p">)</span></span><a href="#l1438"></a>
<span id="l1439">        <span class="bp">self</span><span class="o">.</span><span class="n">_tail</span> <span class="o">=</span> <span class="mi">1</span></span><a href="#l1439"></a>
<span id="l1440">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_last</span></span><a href="#l1440"></a>
<span id="l1441"></span><a href="#l1441"></a>
<span id="l1442"><span class="c">##</span></span><a href="#l1442"></a>
<span id="l1443"><span class="c"># Element structure builder for XML source data, based on the</span></span><a href="#l1443"></a>
<span id="l1444"><span class="c"># &lt;b&gt;expat&lt;/b&gt; parser.</span></span><a href="#l1444"></a>
<span id="l1445"><span class="c">#</span></span><a href="#l1445"></a>
<span id="l1446"><span class="c"># @keyparam target Target object.  If omitted, the builder uses an</span></span><a href="#l1446"></a>
<span id="l1447"><span class="c">#     instance of the standard {@link #TreeBuilder} class.</span></span><a href="#l1447"></a>
<span id="l1448"><span class="c"># @keyparam html Predefine HTML entities.  This flag is not supported</span></span><a href="#l1448"></a>
<span id="l1449"><span class="c">#     by the current implementation.</span></span><a href="#l1449"></a>
<span id="l1450"><span class="c"># @keyparam encoding Optional encoding.  If given, the value overrides</span></span><a href="#l1450"></a>
<span id="l1451"><span class="c">#     the encoding specified in the XML file.</span></span><a href="#l1451"></a>
<span id="l1452"><span class="c"># @see #ElementTree</span></span><a href="#l1452"></a>
<span id="l1453"><span class="c"># @see #TreeBuilder</span></span><a href="#l1453"></a>
<span id="l1454"></span><a href="#l1454"></a>
<span id="l1455"><span class="k">class</span> <span class="nc">XMLParser</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></span><a href="#l1455"></a>
<span id="l1456"></span><a href="#l1456"></a>
<span id="l1457">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">html</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">target</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l1457"></a>
<span id="l1458">        <span class="k">try</span><span class="p">:</span></span><a href="#l1458"></a>
<span id="l1459">            <span class="kn">from</span> <span class="nn">xml.parsers</span> <span class="kn">import</span> <span class="n">expat</span></span><a href="#l1459"></a>
<span id="l1460">        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span></span><a href="#l1460"></a>
<span id="l1461">            <span class="k">try</span><span class="p">:</span></span><a href="#l1461"></a>
<span id="l1462">                <span class="kn">import</span> <span class="nn">pyexpat</span> <span class="kn">as</span> <span class="nn">expat</span></span><a href="#l1462"></a>
<span id="l1463">            <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span></span><a href="#l1463"></a>
<span id="l1464">                <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span></span><a href="#l1464"></a>
<span id="l1465">                    <span class="s">&quot;No module named expat; use SimpleXMLTreeBuilder instead&quot;</span></span><a href="#l1465"></a>
<span id="l1466">                    <span class="p">)</span></span><a href="#l1466"></a>
<span id="l1467">        <span class="n">parser</span> <span class="o">=</span> <span class="n">expat</span><span class="o">.</span><span class="n">ParserCreate</span><span class="p">(</span><span class="n">encoding</span><span class="p">,</span> <span class="s">&quot;}&quot;</span><span class="p">)</span></span><a href="#l1467"></a>
<span id="l1468">        <span class="k">if</span> <span class="n">target</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1468"></a>
<span id="l1469">            <span class="n">target</span> <span class="o">=</span> <span class="n">TreeBuilder</span><span class="p">()</span></span><a href="#l1469"></a>
<span id="l1470">        <span class="c"># underscored names are provided for compatibility only</span></span><a href="#l1470"></a>
<span id="l1471">        <span class="bp">self</span><span class="o">.</span><span class="n">parser</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser</span> <span class="o">=</span> <span class="n">parser</span></span><a href="#l1471"></a>
<span id="l1472">        <span class="bp">self</span><span class="o">.</span><span class="n">target</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_target</span> <span class="o">=</span> <span class="n">target</span></span><a href="#l1472"></a>
<span id="l1473">        <span class="bp">self</span><span class="o">.</span><span class="n">_error</span> <span class="o">=</span> <span class="n">expat</span><span class="o">.</span><span class="n">error</span></span><a href="#l1473"></a>
<span id="l1474">        <span class="bp">self</span><span class="o">.</span><span class="n">_names</span> <span class="o">=</span> <span class="p">{}</span> <span class="c"># name memo cache</span></span><a href="#l1474"></a>
<span id="l1475">        <span class="c"># callbacks</span></span><a href="#l1475"></a>
<span id="l1476">        <span class="n">parser</span><span class="o">.</span><span class="n">DefaultHandlerExpand</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_default</span></span><a href="#l1476"></a>
<span id="l1477">        <span class="n">parser</span><span class="o">.</span><span class="n">StartElementHandler</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_start</span></span><a href="#l1477"></a>
<span id="l1478">        <span class="n">parser</span><span class="o">.</span><span class="n">EndElementHandler</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_end</span></span><a href="#l1478"></a>
<span id="l1479">        <span class="n">parser</span><span class="o">.</span><span class="n">CharacterDataHandler</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_data</span></span><a href="#l1479"></a>
<span id="l1480">        <span class="c"># optional callbacks</span></span><a href="#l1480"></a>
<span id="l1481">        <span class="n">parser</span><span class="o">.</span><span class="n">CommentHandler</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_comment</span></span><a href="#l1481"></a>
<span id="l1482">        <span class="n">parser</span><span class="o">.</span><span class="n">ProcessingInstructionHandler</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_pi</span></span><a href="#l1482"></a>
<span id="l1483">        <span class="c"># let expat do the buffering, if supported</span></span><a href="#l1483"></a>
<span id="l1484">        <span class="k">try</span><span class="p">:</span></span><a href="#l1484"></a>
<span id="l1485">            <span class="bp">self</span><span class="o">.</span><span class="n">_parser</span><span class="o">.</span><span class="n">buffer_text</span> <span class="o">=</span> <span class="mi">1</span></span><a href="#l1485"></a>
<span id="l1486">        <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span></span><a href="#l1486"></a>
<span id="l1487">            <span class="k">pass</span></span><a href="#l1487"></a>
<span id="l1488">        <span class="c"># use new-style attribute handling, if supported</span></span><a href="#l1488"></a>
<span id="l1489">        <span class="k">try</span><span class="p">:</span></span><a href="#l1489"></a>
<span id="l1490">            <span class="bp">self</span><span class="o">.</span><span class="n">_parser</span><span class="o">.</span><span class="n">ordered_attributes</span> <span class="o">=</span> <span class="mi">1</span></span><a href="#l1490"></a>
<span id="l1491">            <span class="bp">self</span><span class="o">.</span><span class="n">_parser</span><span class="o">.</span><span class="n">specified_attributes</span> <span class="o">=</span> <span class="mi">1</span></span><a href="#l1491"></a>
<span id="l1492">            <span class="n">parser</span><span class="o">.</span><span class="n">StartElementHandler</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_start_list</span></span><a href="#l1492"></a>
<span id="l1493">        <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span></span><a href="#l1493"></a>
<span id="l1494">            <span class="k">pass</span></span><a href="#l1494"></a>
<span id="l1495">        <span class="bp">self</span><span class="o">.</span><span class="n">_doctype</span> <span class="o">=</span> <span class="bp">None</span></span><a href="#l1495"></a>
<span id="l1496">        <span class="bp">self</span><span class="o">.</span><span class="n">entity</span> <span class="o">=</span> <span class="p">{}</span></span><a href="#l1496"></a>
<span id="l1497">        <span class="k">try</span><span class="p">:</span></span><a href="#l1497"></a>
<span id="l1498">            <span class="bp">self</span><span class="o">.</span><span class="n">version</span> <span class="o">=</span> <span class="s">&quot;Expat </span><span class="si">%d</span><span class="s">.</span><span class="si">%d</span><span class="s">.</span><span class="si">%d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="n">expat</span><span class="o">.</span><span class="n">version_info</span></span><a href="#l1498"></a>
<span id="l1499">        <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span></span><a href="#l1499"></a>
<span id="l1500">            <span class="k">pass</span> <span class="c"># unknown</span></span><a href="#l1500"></a>
<span id="l1501"></span><a href="#l1501"></a>
<span id="l1502">    <span class="k">def</span> <span class="nf">_raiseerror</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">value</span><span class="p">):</span></span><a href="#l1502"></a>
<span id="l1503">        <span class="n">err</span> <span class="o">=</span> <span class="n">ParseError</span><span class="p">(</span><span class="n">value</span><span class="p">)</span></span><a href="#l1503"></a>
<span id="l1504">        <span class="n">err</span><span class="o">.</span><span class="n">code</span> <span class="o">=</span> <span class="n">value</span><span class="o">.</span><span class="n">code</span></span><a href="#l1504"></a>
<span id="l1505">        <span class="n">err</span><span class="o">.</span><span class="n">position</span> <span class="o">=</span> <span class="n">value</span><span class="o">.</span><span class="n">lineno</span><span class="p">,</span> <span class="n">value</span><span class="o">.</span><span class="n">offset</span></span><a href="#l1505"></a>
<span id="l1506">        <span class="k">raise</span> <span class="n">err</span></span><a href="#l1506"></a>
<span id="l1507"></span><a href="#l1507"></a>
<span id="l1508">    <span class="k">def</span> <span class="nf">_fixtext</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">):</span></span><a href="#l1508"></a>
<span id="l1509">        <span class="c"># convert text string to ascii, if possible</span></span><a href="#l1509"></a>
<span id="l1510">        <span class="k">try</span><span class="p">:</span></span><a href="#l1510"></a>
<span id="l1511">            <span class="k">return</span> <span class="n">text</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="s">&quot;ascii&quot;</span><span class="p">)</span></span><a href="#l1511"></a>
<span id="l1512">        <span class="k">except</span> <span class="ne">UnicodeError</span><span class="p">:</span></span><a href="#l1512"></a>
<span id="l1513">            <span class="k">return</span> <span class="n">text</span></span><a href="#l1513"></a>
<span id="l1514"></span><a href="#l1514"></a>
<span id="l1515">    <span class="k">def</span> <span class="nf">_fixname</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">):</span></span><a href="#l1515"></a>
<span id="l1516">        <span class="c"># expand qname, and convert name string to ascii, if possible</span></span><a href="#l1516"></a>
<span id="l1517">        <span class="k">try</span><span class="p">:</span></span><a href="#l1517"></a>
<span id="l1518">            <span class="n">name</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_names</span><span class="p">[</span><span class="n">key</span><span class="p">]</span></span><a href="#l1518"></a>
<span id="l1519">        <span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span></span><a href="#l1519"></a>
<span id="l1520">            <span class="n">name</span> <span class="o">=</span> <span class="n">key</span></span><a href="#l1520"></a>
<span id="l1521">            <span class="k">if</span> <span class="s">&quot;}&quot;</span> <span class="ow">in</span> <span class="n">name</span><span class="p">:</span></span><a href="#l1521"></a>
<span id="l1522">                <span class="n">name</span> <span class="o">=</span> <span class="s">&quot;{&quot;</span> <span class="o">+</span> <span class="n">name</span></span><a href="#l1522"></a>
<span id="l1523">            <span class="bp">self</span><span class="o">.</span><span class="n">_names</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="n">name</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_fixtext</span><span class="p">(</span><span class="n">name</span><span class="p">)</span></span><a href="#l1523"></a>
<span id="l1524">        <span class="k">return</span> <span class="n">name</span></span><a href="#l1524"></a>
<span id="l1525"></span><a href="#l1525"></a>
<span id="l1526">    <span class="k">def</span> <span class="nf">_start</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tag</span><span class="p">,</span> <span class="n">attrib_in</span><span class="p">):</span></span><a href="#l1526"></a>
<span id="l1527">        <span class="n">fixname</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_fixname</span></span><a href="#l1527"></a>
<span id="l1528">        <span class="n">fixtext</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_fixtext</span></span><a href="#l1528"></a>
<span id="l1529">        <span class="n">tag</span> <span class="o">=</span> <span class="n">fixname</span><span class="p">(</span><span class="n">tag</span><span class="p">)</span></span><a href="#l1529"></a>
<span id="l1530">        <span class="n">attrib</span> <span class="o">=</span> <span class="p">{}</span></span><a href="#l1530"></a>
<span id="l1531">        <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">attrib_in</span><span class="o">.</span><span class="n">items</span><span class="p">():</span></span><a href="#l1531"></a>
<span id="l1532">            <span class="n">attrib</span><span class="p">[</span><span class="n">fixname</span><span class="p">(</span><span class="n">key</span><span class="p">)]</span> <span class="o">=</span> <span class="n">fixtext</span><span class="p">(</span><span class="n">value</span><span class="p">)</span></span><a href="#l1532"></a>
<span id="l1533">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">target</span><span class="o">.</span><span class="n">start</span><span class="p">(</span><span class="n">tag</span><span class="p">,</span> <span class="n">attrib</span><span class="p">)</span></span><a href="#l1533"></a>
<span id="l1534"></span><a href="#l1534"></a>
<span id="l1535">    <span class="k">def</span> <span class="nf">_start_list</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tag</span><span class="p">,</span> <span class="n">attrib_in</span><span class="p">):</span></span><a href="#l1535"></a>
<span id="l1536">        <span class="n">fixname</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_fixname</span></span><a href="#l1536"></a>
<span id="l1537">        <span class="n">fixtext</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_fixtext</span></span><a href="#l1537"></a>
<span id="l1538">        <span class="n">tag</span> <span class="o">=</span> <span class="n">fixname</span><span class="p">(</span><span class="n">tag</span><span class="p">)</span></span><a href="#l1538"></a>
<span id="l1539">        <span class="n">attrib</span> <span class="o">=</span> <span class="p">{}</span></span><a href="#l1539"></a>
<span id="l1540">        <span class="k">if</span> <span class="n">attrib_in</span><span class="p">:</span></span><a href="#l1540"></a>
<span id="l1541">            <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">attrib_in</span><span class="p">),</span> <span class="mi">2</span><span class="p">):</span></span><a href="#l1541"></a>
<span id="l1542">                <span class="n">attrib</span><span class="p">[</span><span class="n">fixname</span><span class="p">(</span><span class="n">attrib_in</span><span class="p">[</span><span class="n">i</span><span class="p">])]</span> <span class="o">=</span> <span class="n">fixtext</span><span class="p">(</span><span class="n">attrib_in</span><span class="p">[</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="p">])</span></span><a href="#l1542"></a>
<span id="l1543">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">target</span><span class="o">.</span><span class="n">start</span><span class="p">(</span><span class="n">tag</span><span class="p">,</span> <span class="n">attrib</span><span class="p">)</span></span><a href="#l1543"></a>
<span id="l1544"></span><a href="#l1544"></a>
<span id="l1545">    <span class="k">def</span> <span class="nf">_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">):</span></span><a href="#l1545"></a>
<span id="l1546">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">target</span><span class="o">.</span><span class="n">data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_fixtext</span><span class="p">(</span><span class="n">text</span><span class="p">))</span></span><a href="#l1546"></a>
<span id="l1547"></span><a href="#l1547"></a>
<span id="l1548">    <span class="k">def</span> <span class="nf">_end</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tag</span><span class="p">):</span></span><a href="#l1548"></a>
<span id="l1549">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">target</span><span class="o">.</span><span class="n">end</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_fixname</span><span class="p">(</span><span class="n">tag</span><span class="p">))</span></span><a href="#l1549"></a>
<span id="l1550"></span><a href="#l1550"></a>
<span id="l1551">    <span class="k">def</span> <span class="nf">_comment</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span></span><a href="#l1551"></a>
<span id="l1552">        <span class="k">try</span><span class="p">:</span></span><a href="#l1552"></a>
<span id="l1553">            <span class="n">comment</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">target</span><span class="o">.</span><span class="n">comment</span></span><a href="#l1553"></a>
<span id="l1554">        <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span></span><a href="#l1554"></a>
<span id="l1555">            <span class="k">pass</span></span><a href="#l1555"></a>
<span id="l1556">        <span class="k">else</span><span class="p">:</span></span><a href="#l1556"></a>
<span id="l1557">            <span class="k">return</span> <span class="n">comment</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_fixtext</span><span class="p">(</span><span class="n">data</span><span class="p">))</span></span><a href="#l1557"></a>
<span id="l1558"></span><a href="#l1558"></a>
<span id="l1559">    <span class="k">def</span> <span class="nf">_pi</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">target</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span></span><a href="#l1559"></a>
<span id="l1560">        <span class="k">try</span><span class="p">:</span></span><a href="#l1560"></a>
<span id="l1561">            <span class="n">pi</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">target</span><span class="o">.</span><span class="n">pi</span></span><a href="#l1561"></a>
<span id="l1562">        <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span></span><a href="#l1562"></a>
<span id="l1563">            <span class="k">pass</span></span><a href="#l1563"></a>
<span id="l1564">        <span class="k">else</span><span class="p">:</span></span><a href="#l1564"></a>
<span id="l1565">            <span class="k">return</span> <span class="n">pi</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_fixtext</span><span class="p">(</span><span class="n">target</span><span class="p">),</span> <span class="bp">self</span><span class="o">.</span><span class="n">_fixtext</span><span class="p">(</span><span class="n">data</span><span class="p">))</span></span><a href="#l1565"></a>
<span id="l1566"></span><a href="#l1566"></a>
<span id="l1567">    <span class="k">def</span> <span class="nf">_default</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">):</span></span><a href="#l1567"></a>
<span id="l1568">        <span class="n">prefix</span> <span class="o">=</span> <span class="n">text</span><span class="p">[:</span><span class="mi">1</span><span class="p">]</span></span><a href="#l1568"></a>
<span id="l1569">        <span class="k">if</span> <span class="n">prefix</span> <span class="o">==</span> <span class="s">&quot;&amp;&quot;</span><span class="p">:</span></span><a href="#l1569"></a>
<span id="l1570">            <span class="c"># deal with undefined entities</span></span><a href="#l1570"></a>
<span id="l1571">            <span class="k">try</span><span class="p">:</span></span><a href="#l1571"></a>
<span id="l1572">                <span class="bp">self</span><span class="o">.</span><span class="n">target</span><span class="o">.</span><span class="n">data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">entity</span><span class="p">[</span><span class="n">text</span><span class="p">[</span><span class="mi">1</span><span class="p">:</span><span class="o">-</span><span class="mi">1</span><span class="p">]])</span></span><a href="#l1572"></a>
<span id="l1573">            <span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span></span><a href="#l1573"></a>
<span id="l1574">                <span class="kn">from</span> <span class="nn">xml.parsers</span> <span class="kn">import</span> <span class="n">expat</span></span><a href="#l1574"></a>
<span id="l1575">                <span class="n">err</span> <span class="o">=</span> <span class="n">expat</span><span class="o">.</span><span class="n">error</span><span class="p">(</span></span><a href="#l1575"></a>
<span id="l1576">                    <span class="s">&quot;undefined entity </span><span class="si">%s</span><span class="s">: line </span><span class="si">%d</span><span class="s">, column </span><span class="si">%d</span><span class="s">&quot;</span> <span class="o">%</span></span><a href="#l1576"></a>
<span id="l1577">                    <span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser</span><span class="o">.</span><span class="n">ErrorLineNumber</span><span class="p">,</span></span><a href="#l1577"></a>
<span id="l1578">                    <span class="bp">self</span><span class="o">.</span><span class="n">_parser</span><span class="o">.</span><span class="n">ErrorColumnNumber</span><span class="p">)</span></span><a href="#l1578"></a>
<span id="l1579">                    <span class="p">)</span></span><a href="#l1579"></a>
<span id="l1580">                <span class="n">err</span><span class="o">.</span><span class="n">code</span> <span class="o">=</span> <span class="mi">11</span> <span class="c"># XML_ERROR_UNDEFINED_ENTITY</span></span><a href="#l1580"></a>
<span id="l1581">                <span class="n">err</span><span class="o">.</span><span class="n">lineno</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser</span><span class="o">.</span><span class="n">ErrorLineNumber</span></span><a href="#l1581"></a>
<span id="l1582">                <span class="n">err</span><span class="o">.</span><span class="n">offset</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser</span><span class="o">.</span><span class="n">ErrorColumnNumber</span></span><a href="#l1582"></a>
<span id="l1583">                <span class="k">raise</span> <span class="n">err</span></span><a href="#l1583"></a>
<span id="l1584">        <span class="k">elif</span> <span class="n">prefix</span> <span class="o">==</span> <span class="s">&quot;&lt;&quot;</span> <span class="ow">and</span> <span class="n">text</span><span class="p">[:</span><span class="mi">9</span><span class="p">]</span> <span class="o">==</span> <span class="s">&quot;&lt;!DOCTYPE&quot;</span><span class="p">:</span></span><a href="#l1584"></a>
<span id="l1585">            <span class="bp">self</span><span class="o">.</span><span class="n">_doctype</span> <span class="o">=</span> <span class="p">[]</span> <span class="c"># inside a doctype declaration</span></span><a href="#l1585"></a>
<span id="l1586">        <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">_doctype</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1586"></a>
<span id="l1587">            <span class="c"># parse doctype contents</span></span><a href="#l1587"></a>
<span id="l1588">            <span class="k">if</span> <span class="n">prefix</span> <span class="o">==</span> <span class="s">&quot;&gt;&quot;</span><span class="p">:</span></span><a href="#l1588"></a>
<span id="l1589">                <span class="bp">self</span><span class="o">.</span><span class="n">_doctype</span> <span class="o">=</span> <span class="bp">None</span></span><a href="#l1589"></a>
<span id="l1590">                <span class="k">return</span></span><a href="#l1590"></a>
<span id="l1591">            <span class="n">text</span> <span class="o">=</span> <span class="n">text</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span></span><a href="#l1591"></a>
<span id="l1592">            <span class="k">if</span> <span class="ow">not</span> <span class="n">text</span><span class="p">:</span></span><a href="#l1592"></a>
<span id="l1593">                <span class="k">return</span></span><a href="#l1593"></a>
<span id="l1594">            <span class="bp">self</span><span class="o">.</span><span class="n">_doctype</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">text</span><span class="p">)</span></span><a href="#l1594"></a>
<span id="l1595">            <span class="n">n</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_doctype</span><span class="p">)</span></span><a href="#l1595"></a>
<span id="l1596">            <span class="k">if</span> <span class="n">n</span> <span class="o">&gt;</span> <span class="mi">2</span><span class="p">:</span></span><a href="#l1596"></a>
<span id="l1597">                <span class="nb">type</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_doctype</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span></span><a href="#l1597"></a>
<span id="l1598">                <span class="k">if</span> <span class="nb">type</span> <span class="o">==</span> <span class="s">&quot;PUBLIC&quot;</span> <span class="ow">and</span> <span class="n">n</span> <span class="o">==</span> <span class="mi">4</span><span class="p">:</span></span><a href="#l1598"></a>
<span id="l1599">                    <span class="n">name</span><span class="p">,</span> <span class="nb">type</span><span class="p">,</span> <span class="n">pubid</span><span class="p">,</span> <span class="n">system</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_doctype</span></span><a href="#l1599"></a>
<span id="l1600">                <span class="k">elif</span> <span class="nb">type</span> <span class="o">==</span> <span class="s">&quot;SYSTEM&quot;</span> <span class="ow">and</span> <span class="n">n</span> <span class="o">==</span> <span class="mi">3</span><span class="p">:</span></span><a href="#l1600"></a>
<span id="l1601">                    <span class="n">name</span><span class="p">,</span> <span class="nb">type</span><span class="p">,</span> <span class="n">system</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_doctype</span></span><a href="#l1601"></a>
<span id="l1602">                    <span class="n">pubid</span> <span class="o">=</span> <span class="bp">None</span></span><a href="#l1602"></a>
<span id="l1603">                <span class="k">else</span><span class="p">:</span></span><a href="#l1603"></a>
<span id="l1604">                    <span class="k">return</span></span><a href="#l1604"></a>
<span id="l1605">                <span class="k">if</span> <span class="n">pubid</span><span class="p">:</span></span><a href="#l1605"></a>
<span id="l1606">                    <span class="n">pubid</span> <span class="o">=</span> <span class="n">pubid</span><span class="p">[</span><span class="mi">1</span><span class="p">:</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span></span><a href="#l1606"></a>
<span id="l1607">                <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">target</span><span class="p">,</span> <span class="s">&quot;doctype&quot;</span><span class="p">):</span></span><a href="#l1607"></a>
<span id="l1608">                    <span class="bp">self</span><span class="o">.</span><span class="n">target</span><span class="o">.</span><span class="n">doctype</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">pubid</span><span class="p">,</span> <span class="n">system</span><span class="p">[</span><span class="mi">1</span><span class="p">:</span><span class="o">-</span><span class="mi">1</span><span class="p">])</span></span><a href="#l1608"></a>
<span id="l1609">                <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">doctype</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_XMLParser__doctype</span><span class="p">:</span></span><a href="#l1609"></a>
<span id="l1610">                    <span class="c"># warn about deprecated call</span></span><a href="#l1610"></a>
<span id="l1611">                    <span class="bp">self</span><span class="o">.</span><span class="n">_XMLParser__doctype</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">pubid</span><span class="p">,</span> <span class="n">system</span><span class="p">[</span><span class="mi">1</span><span class="p">:</span><span class="o">-</span><span class="mi">1</span><span class="p">])</span></span><a href="#l1611"></a>
<span id="l1612">                    <span class="bp">self</span><span class="o">.</span><span class="n">doctype</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">pubid</span><span class="p">,</span> <span class="n">system</span><span class="p">[</span><span class="mi">1</span><span class="p">:</span><span class="o">-</span><span class="mi">1</span><span class="p">])</span></span><a href="#l1612"></a>
<span id="l1613">                <span class="bp">self</span><span class="o">.</span><span class="n">_doctype</span> <span class="o">=</span> <span class="bp">None</span></span><a href="#l1613"></a>
<span id="l1614"></span><a href="#l1614"></a>
<span id="l1615">    <span class="c">##</span></span><a href="#l1615"></a>
<span id="l1616">    <span class="c"># (Deprecated) Handles a doctype declaration.</span></span><a href="#l1616"></a>
<span id="l1617">    <span class="c">#</span></span><a href="#l1617"></a>
<span id="l1618">    <span class="c"># @param name Doctype name.</span></span><a href="#l1618"></a>
<span id="l1619">    <span class="c"># @param pubid Public identifier.</span></span><a href="#l1619"></a>
<span id="l1620">    <span class="c"># @param system System identifier.</span></span><a href="#l1620"></a>
<span id="l1621"></span><a href="#l1621"></a>
<span id="l1622">    <span class="k">def</span> <span class="nf">doctype</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">pubid</span><span class="p">,</span> <span class="n">system</span><span class="p">):</span></span><a href="#l1622"></a>
<span id="l1623">        <span class="sd">&quot;&quot;&quot;This method of XMLParser is deprecated.&quot;&quot;&quot;</span></span><a href="#l1623"></a>
<span id="l1624">        <span class="n">warnings</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span></span><a href="#l1624"></a>
<span id="l1625">            <span class="s">&quot;This method of XMLParser is deprecated.  Define doctype() &quot;</span></span><a href="#l1625"></a>
<span id="l1626">            <span class="s">&quot;method on the TreeBuilder target.&quot;</span><span class="p">,</span></span><a href="#l1626"></a>
<span id="l1627">            <span class="ne">DeprecationWarning</span><span class="p">,</span></span><a href="#l1627"></a>
<span id="l1628">            <span class="p">)</span></span><a href="#l1628"></a>
<span id="l1629"></span><a href="#l1629"></a>
<span id="l1630">    <span class="c"># sentinel, if doctype is redefined in a subclass</span></span><a href="#l1630"></a>
<span id="l1631">    <span class="n">__doctype</span> <span class="o">=</span> <span class="n">doctype</span></span><a href="#l1631"></a>
<span id="l1632"></span><a href="#l1632"></a>
<span id="l1633">    <span class="c">##</span></span><a href="#l1633"></a>
<span id="l1634">    <span class="c"># Feeds data to the parser.</span></span><a href="#l1634"></a>
<span id="l1635">    <span class="c">#</span></span><a href="#l1635"></a>
<span id="l1636">    <span class="c"># @param data Encoded data.</span></span><a href="#l1636"></a>
<span id="l1637"></span><a href="#l1637"></a>
<span id="l1638">    <span class="k">def</span> <span class="nf">feed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span></span><a href="#l1638"></a>
<span id="l1639">        <span class="k">try</span><span class="p">:</span></span><a href="#l1639"></a>
<span id="l1640">            <span class="bp">self</span><span class="o">.</span><span class="n">_parser</span><span class="o">.</span><span class="n">Parse</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span></span><a href="#l1640"></a>
<span id="l1641">        <span class="k">except</span> <span class="bp">self</span><span class="o">.</span><span class="n">_error</span><span class="p">,</span> <span class="n">v</span><span class="p">:</span></span><a href="#l1641"></a>
<span id="l1642">            <span class="bp">self</span><span class="o">.</span><span class="n">_raiseerror</span><span class="p">(</span><span class="n">v</span><span class="p">)</span></span><a href="#l1642"></a>
<span id="l1643"></span><a href="#l1643"></a>
<span id="l1644">    <span class="c">##</span></span><a href="#l1644"></a>
<span id="l1645">    <span class="c"># Finishes feeding data to the parser.</span></span><a href="#l1645"></a>
<span id="l1646">    <span class="c">#</span></span><a href="#l1646"></a>
<span id="l1647">    <span class="c"># @return An element structure.</span></span><a href="#l1647"></a>
<span id="l1648">    <span class="c"># @defreturn Element</span></span><a href="#l1648"></a>
<span id="l1649"></span><a href="#l1649"></a>
<span id="l1650">    <span class="k">def</span> <span class="nf">close</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1650"></a>
<span id="l1651">        <span class="k">try</span><span class="p">:</span></span><a href="#l1651"></a>
<span id="l1652">            <span class="bp">self</span><span class="o">.</span><span class="n">_parser</span><span class="o">.</span><span class="n">Parse</span><span class="p">(</span><span class="s">&quot;&quot;</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span> <span class="c"># end of data</span></span><a href="#l1652"></a>
<span id="l1653">        <span class="k">except</span> <span class="bp">self</span><span class="o">.</span><span class="n">_error</span><span class="p">,</span> <span class="n">v</span><span class="p">:</span></span><a href="#l1653"></a>
<span id="l1654">            <span class="bp">self</span><span class="o">.</span><span class="n">_raiseerror</span><span class="p">(</span><span class="n">v</span><span class="p">)</span></span><a href="#l1654"></a>
<span id="l1655">        <span class="n">tree</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">target</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></span><a href="#l1655"></a>
<span id="l1656">        <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">target</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser</span> <span class="c"># get rid of circular references</span></span><a href="#l1656"></a>
<span id="l1657">        <span class="k">return</span> <span class="n">tree</span></span><a href="#l1657"></a>
<span id="l1658"></span><a href="#l1658"></a>
<span id="l1659"><span class="c"># compatibility</span></span><a href="#l1659"></a>
<span id="l1660"><span class="n">XMLTreeBuilder</span> <span class="o">=</span> <span class="n">XMLParser</span></span><a href="#l1660"></a>
<span id="l1661"></span><a href="#l1661"></a>
<span id="l1662"><span class="c"># workaround circular import.</span></span><a href="#l1662"></a>
<span id="l1663"><span class="k">try</span><span class="p">:</span></span><a href="#l1663"></a>
<span id="l1664">    <span class="kn">from</span> <span class="nn">ElementC14N</span> <span class="kn">import</span> <span class="n">_serialize_c14n</span></span><a href="#l1664"></a>
<span id="l1665">    <span class="n">_serialize</span><span class="p">[</span><span class="s">&quot;c14n&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">_serialize_c14n</span></span><a href="#l1665"></a>
<span id="l1666"><span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span></span><a href="#l1666"></a>
<span id="l1667">    <span class="k">pass</span></span><a href="#l1667"></a></pre>
<div class="sourcelast"></div>
</div>
</div>
</div>

<script type="text/javascript">process_dates()</script>


</body>
</html>

