function encodeAndDecodeMessages() {
    let encodeBtn = document.getElementsByTagName('button')[0];
    let decodeBtn = document.getElementsByTagName('button')[1];
    
    let encodeParent = encodeBtn.parentNode;
    let decodeParent = decodeBtn.parentNode;

    let messageEncode = encodeParent.querySelector('textarea');
    let messageDecode = decodeParent.querySelector('textarea');

    encodeBtn.addEventListener('click', encodeFnc);
    decodeParent.addEventListener('click', decodeFnc);

    function encodeFnc(e) {

        let listEncode = [];
        

        for (const char of messageEncode.value) {


            nextChar = char.charCodeAt(0) + 1;
            newStr = String.fromCharCode(nextChar);
            listEncode.push(newStr);
   
        }

        messageDecode.value = listEncode.join('');
        messageEncode.value = '';
        
    }

    function decodeFnc(e) {

        let listDecode = [];

        for (const char of messageDecode.value) {
            nextChar = char.charCodeAt(0) - 1;
            newStr = String.fromCharCode(nextChar);
            listDecode.push(newStr);
        }

        messageDecode.value = listDecode.join('');

    }
  
}