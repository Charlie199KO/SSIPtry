function proceed() {
    if (document.getElementById('key').value == " ") {
        document.getElementById('information_section').classList.remove("temporaryly_disabled")
        document.getElementById('key_section').classList.add('temporaryly_disabled')
    }
    else {
        alert("Sorry! The key is wrong\nPlease Try Again")
    }
}

function jump() {
    if (document.getElementById('email_address').value == "") {
        alert("Required! \nPlease Enter Your Email Address")
    }
    else if (document.getElementById('phone_number').value == "") {
        alert('Required! \nPlease Enter Your Phone Number')
    }
    else {
        document.getElementById('jump_button').classList.add("temporaryly_disabled")
        document.getElementById('detail_section').classList.remove('temporaryly_disabled')
    }
}

function next() {
    if (document.getElementById('district').value == "Select_Your_District") {
        alert('Required! \nPlease Select Your District')
    }
    else if (document.getElementById('police_station_name').value == "") {
        alert('Required! \nPlease Enter Your Police Station Name')
    }
    else {
        document.getElementById('signup_section').classList.remove('temporaryly_disabled')
        document.getElementById('next_button').classList.add("temporaryly_disabled")
    }
}

function signup() {
    if (document.getElementById('username').value == "") {
        alert("Required! \nPlease Enter Your Username")
    }
    else if (document.getElementById('password').value == "") {
        alert("Required! \nPlease Enter Your Password")
    }
    else {
        confirmation()
    }
}

function confirmation() {
    alert('You Are Proceeding Towards SignUp')
    sub()
}

function sub() {
    document.getElementById('signup_form').submit()
}

function _selected_c(){
    x = document.getElementById('district').value
    document.getElementById('selected_city').value = x
    console.log(document.getElementById('selected_city').value)
}