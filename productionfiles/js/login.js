function check() {
    if (document.getElementById('username').value == "") {
        alert("Required! \nPlease Enter Your Username")
    }
    else if (document.getElementById('password').value == 0) {
        alert("Required! \nPlease Enter The Password")
    }
    else {
        confirmation()
}
}

function confirmation() {
    alert('You Are Proceeding Towards LogIn')
    sub()
}


function sub() {
    document.getElementById('login_form').submit()
}