import base64
from urllib.parse import unquote, quote

"""
function xor_encrypt($in) {
    $key = '<censored>';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}
"""
def xor_encrypt(text):
    key = 'qw8J'
    out_text = ''
    for i in range(0, len(text)):
        # print("test: " + text[i])
        out_text += chr(text[i] ^ ord((key[i % len(key)])))
    return out_text


def xor_getkey(a, b):
    out = ''
    for x, y in zip(a,b):
        out += chr(x ^ y)
    return out


"""
function loadData($def) {
    global $_COOKIE;
    $mydata = $def;
    if(array_key_exists("data", $_COOKIE)) {
    $tempdata = json_decode(xor_encrypt(base64_decode($_COOKIE["data"])), true);
    if(is_array($tempdata) && array_key_exists("showpassword", $tempdata) && array_key_exists("bgcolor", $tempdata)) {
        if (preg_match('/^#(?:[a-f\d]{6})$/i', $tempdata['bgcolor'])) {
        $mydata['showpassword'] = $tempdata['showpassword'];
        $mydata['bgcolor'] = $tempdata['bgcolor'];
        }
    }
    }
    return $mydata;
}
"""

def decode(cookie):
    return xor_encrypt(base64.b64decode(unquote(cookie)))

def get_key(cookie, og_data):
    return xor_getkey(base64.b64decode(unquote(cookie)), og_data)

def get_cookie(json):
    return quote(base64.b64encode(xor_encrypt(json).encode()))

# print(xor_encrypt())
print(get_key('ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSRwh6QEULaAw%3D', b'{"showpassword":"no","bgcolor":"#000123"}'))
print(decode('ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSRwh6QEULaAw%3D'))
print(get_cookie(b'{"showpassword":"yes","bgcolor":"#000123"}'))
