function next(){
    if (document.getElementById('name').value == ""){
        alert('Required! \nPlease Enter Your Name')
    }
    else if (document.getElementById('email').value == ""){
        alert("Required! \nPlease Enter Your Email")
    }
    else if (document.getElementById('phone_number').value == ""){
        alert("Required! \nPlease Enter Your Phone Number")
    }
    else {
        document.getElementById('compliment_section').classList.remove('temporaryly_disabled')
        document.getElementById('next_button').classList.add('temporaryly_disabled')
    }
}

function proceed(){
    if (document.getElementById('compliment').value == ""){
        alert("Required! \nEnter The Compliment")
    }
    else {
    confirmation()
}
}

function confirmation() {
    alert('You Are Proceeding Towards Submittion')
    sub()
}

function sub() {
    document.getElementById('compliment_form').submit()
}
