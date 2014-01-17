#!/usr/bin/perl

print "Content-type: text/html; charset=utf-8\n\n";

use CGI;
$q=new CGI;

$uname=$q->param('uname');

@katagaki1=("あたらしい","水色の","そよ風","ムキムキ","仏像","粋な","今どきっな","片思いの","桃色");
@katagaki2=("系女子","当番","委員","起爆剤","打ち上げ花火","バックパッカー","キラキラ女子","インターン","反逆児","学会会長","案内人","ヒロイン");

$k1=int(rand(9));
$k2=int(rand(12));


print <<EOF;
<html>
<head>
<title>あたらしい肩書き診断</title>
</head>
<body>

<p>あたらしいインターンによる</p>
<h1>あたらしい肩書き診断</h1>

<form method="POST" action="./katagaki.cgi">
<h3>任意の名前を入力してください</h3>
<input type="text" name="uname" size="30">
<input type="submit" value="診断する">
</form>
EOF

if($uname){
print "<h2>". $uname . "さんのあたらしい肩書きは、　『" . $katagaki1[$k1] . $katagaki2[$k2] . "』　です。</h2>";
}

print "</body>";
print "</html>";


exit 0;