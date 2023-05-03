<h2><a href="https://leetcode.com/problems/sum-root-to-leaf-numbers/">129. Sum Root to Leaf Numbers</a></h2><h3>Medium</h3><hr><div><p>You are given the <code>root</code> of a binary tree containing digits from <code>0</code> to <code>9</code> only.</p>

<p>Each root-to-leaf path in the tree represents a number.</p>

<ul>
	<li>For example, the root-to-leaf path <code>1 -&gt; 2 -&gt; 3</code> represents the number <code>123</code>.</li>
</ul>

<p>Return <em>the total sum of all root-to-leaf numbers</em>. Test cases are generated so that the answer will fit in a <strong>32-bit</strong> integer.</p>

<p>A <strong>leaf</strong> node is a node with no children.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/num1tree.jpg" style="width: 212px; height: 182px;">
<pre class="button-container"><button type="button" class="a2sv-button"><span>a2svify</span></button><button type="button" class="a2sv-button"><span>a2svify</span></button><button type="button" class="a2sv-button"><span>a2svify</span></button><button type="button" class="a2sv-button"><span>a2svify</span></button><button type="button" class="a2sv-button"><span>a2svify</span></button><button type="button" class="a2sv-button"><span>a2svify</span></button><button type="button" class="a2sv-button"><span>a2svify</span></button><button type="button" class="a2sv-button"><span>a2svify</span></button><button type="button" class="a2sv-button"><span>a2svify</span></button><button type="button" class="a2sv-button"><span>a2svify</span></button><button type="button" class="a2sv-button"><span>a2svify</span></button><button type="button" class="a2sv-button"><span>a2svify</span></button><button type="button" class="a2sv-button"><span>a2svify</span></button><button type="button" class="a2sv-button"><span>a2svify</span></button><button type="button" class="a2sv-button"><span>a2svify</span></button><button type="button" class="a2sv-button"><span>a2svify</span></button><button type="button" class="a2sv-button"><span>a2svify</span></button><button type="button" class="a2sv-button"><span>a2svify</span></button><button type="button" class="a2sv-button"><span>a2svify</span></button><button type="button" class="a2sv-button"><span>a2svify</span></button><button type="button" class="a2sv-button" fdprocessedid="0x2zzp"><span>a2svify</span></button><button type="button" class="a2sv-button" fdprocessedid="n4r39xy"><span>a2svify</span></button><button type="button" class="a2sv-button" fdprocessedid="5e8wi"><span>a2svify</span></button><button type="button" class="a2sv-button" fdprocessedid="jkqhr"><span>a2svify</span></button><button type="button" class="a2sv-button" fdprocessedid="ac5rdp"><span>a2svify</span></button><button type="button" class="a2sv-button" fdprocessedid="cc79hm"><span>a2svify</span></button><button type="button" class="a2sv-button" fdprocessedid="qi3gxx"><span>a2svify</span></button><button type="button" class="a2sv-button" fdprocessedid="hgtx7"><span>a2svify</span></button><button type="button" class="a2sv-button" fdprocessedid="z5zza"><span>a2svify</span></button><button type="button" class="a2sv-button" fdprocessedid="yolc6g"><span>a2svify</span></button><button type="button" class="a2sv-button" fdprocessedid="xk1x5"><span>a2svify</span></button><button type="button" class="a2sv-button" fdprocessedid="eqffvt"><span>a2svify</span></button><button type="button" class="a2sv-button" fdprocessedid="t7muk"><span>a2svify</span></button><button type="button" class="a2sv-button" fdprocessedid="gko298"><span>a2svify</span></button><button type="button" class="a2sv-button" fdprocessedid="ui9we8"><span>a2svify</span></button><strong>Input:</strong> root = [1,2,3]
<strong>Output:</strong> 25
<strong>Explanation:</strong>
The root-to-leaf path <code>1-&gt;2</code> represents the number <code>12</code>.
The root-to-leaf path <code>1-&gt;3</code> represents the number <code>13</code>.
Therefore, sum = 12 + 13 = <code>25</code>.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/num2tree.jpg" style="width: 292px; height: 302px;">
<pre class="button-container"><button type="button" class="a2sv-button"><span>a2svify</span></button><button type="button" class="a2sv-button"><span>a2svify</span></button><button type="button" class="a2sv-button"><span>a2svify</span></button><button type="button" class="a2sv-button"><span>a2svify</span></button><button type="button" class="a2sv-button" fdprocessedid="t8d8zd"><span>a2svify</span></button><button type="button" class="a2sv-button" fdprocessedid="ppwc8x"><span>a2svify</span></button><button type="button" class="a2sv-button" fdprocessedid="adm1we"><span>a2svify</span></button><button type="button" class="a2sv-button" fdprocessedid="wa1ia"><span>a2svify</span></button><button type="button" class="a2sv-button" fdprocessedid="8n5l6w"><span>a2svify</span></button><button type="button" class="a2sv-button" fdprocessedid="2bm7cmm"><span>a2svify</span></button><button type="button" class="a2sv-button" fdprocessedid="p6ovkj"><span>a2svify</span></button><button type="button" class="a2sv-button" fdprocessedid="yn5b2o"><span>a2svify</span></button><button type="button" class="a2sv-button" fdprocessedid="navdj"><span>a2svify</span></button><button type="button" class="a2sv-button" fdprocessedid="uf7nx2"><span>a2svify</span></button><button type="button" class="a2sv-button" fdprocessedid="ap5iaw"><span>a2svify</span></button><button type="button" class="a2sv-button" fdprocessedid="chsdj7"><span>a2svify</span></button><button type="button" class="a2sv-button" fdprocessedid="89arbn"><span>a2svify</span></button><button type="button" class="a2sv-button" fdprocessedid="mqy74"><span>a2svify</span></button><button type="button" class="a2sv-button" fdprocessedid="wkwu7k"><span>a2svify</span></button><button type="button" class="a2sv-button" fdprocessedid="0f6yd"><span>a2svify</span></button><button type="button" class="a2sv-button" fdprocessedid="1kbfsh"><span>a2svify</span></button><button type="button" class="a2sv-button" fdprocessedid="9gq0c"><span>a2svify</span></button><button type="button" class="a2sv-button" fdprocessedid="10nz3n"><span>a2svify</span></button><button type="button" class="a2sv-button" fdprocessedid="37mis"><span>a2svify</span></button><button type="button" class="a2sv-button" fdprocessedid="4qcjx5d"><span>a2svify</span></button><button type="button" class="a2sv-button" fdprocessedid="qqgo2l"><span>a2svify</span></button><button type="button" class="a2sv-button" fdprocessedid="mkfv22"><span>a2svify</span></button><button type="button" class="a2sv-button" fdprocessedid="cn63tw"><span>a2svify</span></button><strong>Input:</strong> root = [4,9,0,5,1]
<strong>Output:</strong> 1026
<strong>Explanation:</strong>
The root-to-leaf path <code>4-&gt;9-&gt;5</code> represents the number 495.
The root-to-leaf path <code>4-&gt;9-&gt;1</code> represents the number 491.
The root-to-leaf path <code>4-&gt;0</code> represents the number 40.
Therefore, sum = 495 + 491 + 40 = <code>1026</code>.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 1000]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 9</code></li>
	<li>The depth of the tree will not exceed <code>10</code>.</li>
</ul>
</div>