const display = document.getElementById('display');

function AddToDisplay(input) {
    display.value += input;
}

function clear() {
    console.log("Clear button clicked");
    display.value = "";
}

function calc() {
    try{
        display.value = eval(display.value);
    }
    catch(error) {
        display.value = "Error";
    }
}

/*if user press on Enter*/
document.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        calc();
        event.preventDefault(); // لمنع التصرف الافتراضي مثل الإرسال
    }
});

const clearButton = document.querySelector('button[onclick="clear()"]');
clearButton.addEventListener('click', clear);