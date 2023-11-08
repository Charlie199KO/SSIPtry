function next() {
    if (document.getElementById('name').value == "") {
        alert("Required! \nPlease Enter Your Name")
    }
    else if (document.getElementById('phone_number').value == "") {
        alert('Required! \nPlease Enter Your Phone Number')
    }
    else {
        document.getElementById('incident_section').classList.remove("temporaryly_disabled")
        document.getElementById('next_button').classList.add("temporaryly_disabled")
    }
}

function proceed() {
    if (document.getElementById('location').value == "") {
        alert("Required! \nPlease Enter Your Location To Proceed Further")
    }
    else if (document.getElementById('incident_with').value == "Select_Your_Incident_With") {
        alert("Required! \nPlease Select With Whom The Incident Happened")
    }
    else {
        document.getElementById('written_section').classList.remove("temporaryly_disabled")
        document.getElementById('proceed_button').classList.add("temporaryly_disabled")
    }
}

function check() {
    if (document.getElementById('incident').value == "") {
        alert("Required! \nPlease Enter The Incident")
    }
    else {
        confirmation()
    }
}

function confirmation() {
    alert('You Are proceeding Towards Submittion')
    sub()
}

function sub() {
    document.getElementById('incident_form').submit()
}

function select_incident_with(){
    x = document.getElementById('incident_with').value
    document.getElementById('incident_selected').value = x
}