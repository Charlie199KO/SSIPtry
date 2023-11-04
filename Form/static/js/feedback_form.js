function personal_details(){
    if (document.getElementById('name').value == ""){
        alert('Required! \nYour name is required to proceed')
    }
    else if (document.getElementById('email').value == ""){
        alert('Required! \nYour email is required to proceed')
    }
    else if (document.getElementById('phone_number').value == ""){
        alert('Required! \nYour Phone Number is required to proceed')
    }
    else {
        document.getElementById('select_section').classList.remove('temporaryly_disabled')
        document.getElementById('feedback_next_button1').classList.add('no_display')
    }
}

function check_selection_section(){
    if (document.getElementById("city").value == "Select_Your_City"){
        alert("Required! \nPlease select Your City To Proceed Further")
    }
    //else if (document.getElementById('police_station').value == "Select_Your_Police_Station"){
      //  alert("Required! \nPlease select Police Station To Proceed Further")
    //}
    else{
        document.getElementById('feedback_next_button2').classList.add('no_display')
        document.getElementById('question1_section').classList.remove('temporaryly_disabled')
        document.getElementById('question2_section').classList.remove('temporaryly_disabled')
        document.getElementById('question3_section').classList.remove('temporaryly_disabled')
        document.getElementById('question4_section').classList.remove('temporaryly_disabled')
        document.getElementById('question5_section').classList.remove('temporaryly_disabled')
        document.getElementById('question6_section').classList.remove('temporaryly_disabled')
        document.getElementById('question7_section').classList.remove('temporaryly_disabled')
        document.getElementById('question8_section').classList.remove('temporaryly_disabled')
        document.getElementById('question9_section').classList.remove('temporaryly_disabled')
        document.getElementById('question10_section').classList.remove('temporaryly_disabled')
        document.getElementById('rating_section').classList.remove('temporaryly_disabled')
        document.getElementById('written_feedback_section').classList.remove('temporaryly_disabled')
        document.getElementById('submit_button').classList.remove('temporaryly_disabled')
    }
}

function star_rating(id_of_element_clicked, value) {

    if (id_of_element_clicked == 'star-1'){
        document.getElementById(id_of_element_clicked).style.color = "Orange"
        document.getElementById('star-2').style.color = "Black"
        document.getElementById('star-3').style.color = "Black"
        document.getElementById('star-4').style.color = "Black"
        document.getElementById('star-5').style.color = "Black"
        document.getElementById('star-1').value = 1
    }
    else if (id_of_element_clicked == "star-2"){
        document.getElementById(id_of_element_clicked).style.color = "Orange"
        document.getElementById('star-1').style.color = "Orange"
        document.getElementById('star-3').style.color = "Black"
        document.getElementById('star-4').style.color = "Black"
        document.getElementById('star-5').style.color = "Black"
        document.getElementById('star-1').value = 2
    }     
    else if (id_of_element_clicked == "star-3"){
        document.getElementById(id_of_element_clicked).style.color = "Orange"
        document.getElementById('star-2').style.color = "Orange"
        document.getElementById('star-1').style.color = "Orange"
        document.getElementById('star-4').style.color = "Black"
        document.getElementById('star-5').style.color = "Black"
        document.getElementById('star-1').value = 3
    }
    else if (id_of_element_clicked == 'star-4'){
        document.getElementById(id_of_element_clicked).style.color = "Orange"
        document.getElementById('star-3').style.color = "Orange"
        document.getElementById('star-2').style.color = "Orange"
        document.getElementById('star-1').style.color = "Orange"
        document.getElementById('star-5').style.color = "Black"
        document.getElementById('star-1').value = 4
    }
    else if (id_of_element_clicked == "star-5"){
        document.getElementById(id_of_element_clicked).style.color = "Orange"
        document.getElementById('star-4').style.color = "Orange"
        document.getElementById('star-3').style.color = "Orange"
        document.getElementById('star-2').style.color = "Orange"
        document.getElementById('star-1').style.color = "Orange"
        document.getElementById('star-1').value = 5
    }
}

function star_rating1(id_of_element_clicked1){
    if (id_of_element_clicked1 == '1star'){
        document.getElementById(id_of_element_clicked1).style.color = "Orange"
        document.getElementById('2star').style.color = "Black"
        document.getElementById('3star').style.color = "Black"
        document.getElementById('4star').style.color = "Black"
        document.getElementById('5star').style.color = "Black"
        document.getElementById('1star').value = 1
    }
    else if (id_of_element_clicked1 == '2star'){
        document.getElementById(id_of_element_clicked1).style.color = "Orange"
        document.getElementById('1star').style.color = "Orange"
        document.getElementById('3star').style.color = "Black"
        document.getElementById('4star').style.color = "Black"
        document.getElementById('5star').style.color = "Black"
        document.getElementById('1star').value = 2
    }
    else if (id_of_element_clicked1 == '3star'){
        document.getElementById(id_of_element_clicked1).style.color = "Orange"
        document.getElementById('2star').style.color = "Orange"
        document.getElementById('1star').style.color = "Orange"
        document.getElementById('4star').style.color = "Black"
        document.getElementById('5star').style.color = "Black"
        document.getElementById('1star').value = 3
    }
    else if (id_of_element_clicked1 == '4star'){
        document.getElementById(id_of_element_clicked1).style.color = "Orange"
        document.getElementById('3star').style.color = "Orange"
        document.getElementById('2star').style.color = "Orange"
        document.getElementById('1star').style.color = "Orange"
        document.getElementById('5star').style.color = "Black"
        document.getElementById('1star').value = 4
    }
    else if (id_of_element_clicked1 == '5star'){
        document.getElementById(id_of_element_clicked1).style.color = "Orange"
        document.getElementById('4star').style.color = "Orange"
        document.getElementById('3star').style.color = "Orange"
        document.getElementById('2star').style.color = "Orange"
        document.getElementById('1star').style.color = "Orange"
        document.getElementById('1star').value = 5
    }
}

function required_check(){
    if (document.getElementById('star-1').value == 0){
        alert("Required! \nOverall Rating is required")
    }
    else{
        confirmation()
    }
}

function confirmation(){
    alert('You are procceding towards submittion')
    sub()
}

function star_rating2(id_of_element_clicked2){
    if (id_of_element_clicked2 == '2_1star'){
        document.getElementById(id_of_element_clicked2).style.color = "Orange"
        document.getElementById('2_2star').style.color = "Black"
        document.getElementById('2_3star').style.color = "Black"
        document.getElementById('2_4star').style.color = "Black"
        document.getElementById('2_5star').style.color = "Black"
        document.getElementById('2_1star').value = 1
    }
    else if (id_of_element_clicked2 == '2_2star'){
        document.getElementById(id_of_element_clicked2).style.color = "Orange"
        document.getElementById('2_1star').style.color = "Orange"
        document.getElementById('2_3star').style.color = "Black"
        document.getElementById('2_4star').style.color = "Black"
        document.getElementById('2_5star').style.color = "Black"
        document.getElementById('2_1star').value = 2
    }
    else if (id_of_element_clicked2 == '2_3star'){
        document.getElementById(id_of_element_clicked2).style.color = "Orange"
        document.getElementById('2_2star').style.color = "Orange"
        document.getElementById('2_1star').style.color = "Orange"
        document.getElementById('2_4star').style.color = "Black"
        document.getElementById('2_5star').style.color = "Black"
        document.getElementById('2_1star').value = 3
    }
    else if (id_of_element_clicked2 == '2_4star'){
        document.getElementById(id_of_element_clicked2).style.color = "Orange"
        document.getElementById('2_3star').style.color = "Orange"
        document.getElementById('2_2star').style.color = "Orange"
        document.getElementById('2_1star').style.color = "Orange"
        document.getElementById('2_5star').style.color = "Black"
        document.getElementById('2_1star').value = 4
    }
    else if (id_of_element_clicked2 == '2_5star'){
        document.getElementById(id_of_element_clicked2).style.color = "Orange"
        document.getElementById('2_4star').style.color = "Orange"
        document.getElementById('2_3star').style.color = "Orange"
        document.getElementById('2_2star').style.color = "Orange"
        document.getElementById('2_1star').style.color = "Orange"
        document.getElementById('2_1star').value = 5
    }
}

function star_rating3(id_of_element_clicked3){
    if (id_of_element_clicked3 == '3_1star'){
        document.getElementById(id_of_element_clicked3).style.color = "Orange"
        document.getElementById('3_2star').style.color = "Black"
        document.getElementById('3_3star').style.color = "Black"
        document.getElementById('3_4star').style.color = "Black"
        document.getElementById('3_5star').style.color = "Black"
        document.getElementById('3_1star').value = 1
    }
    else if (id_of_element_clicked3 == '3_2star'){
        document.getElementById(id_of_element_clicked3).style.color = "Orange"
        document.getElementById('3_1star').style.color = "Orange"
        document.getElementById('3_3star').style.color = "Black"
        document.getElementById('3_4star').style.color = "Black"
        document.getElementById('3_5star').style.color = "Black"
        document.getElementById('3_1star').value = 2
    }
    else if (id_of_element_clicked3 == '3_3star'){
        document.getElementById(id_of_element_clicked3).style.color = "Orange"
        document.getElementById('3_2star').style.color = "Orange"
        document.getElementById('3_1star').style.color = "Orange"
        document.getElementById('3_4star').style.color = "Black"
        document.getElementById('3_5star').style.color = "Black"
        document.getElementById('3_1star').value = 3
    }
    else if (id_of_element_clicked3 == '3_4star'){
        document.getElementById(id_of_element_clicked3).style.color = "Orange"
        document.getElementById('3_3star').style.color = "Orange"
        document.getElementById('3_2star').style.color = "Orange"
        document.getElementById('3_1star').style.color = "Orange"
        document.getElementById('3_5star').style.color = "Black"
        document.getElementById('3_1star').value = 4
    }
    else if (id_of_element_clicked3 == '3_5star'){
        document.getElementById(id_of_element_clicked3).style.color = "Orange"
        document.getElementById('3_4star').style.color = "Orange"
        document.getElementById('3_3star').style.color = "Orange"
        document.getElementById('3_2star').style.color = "Orange"
        document.getElementById('3_1star').style.color = "Orange"
        document.getElementById('3_1star').value = 5
    }
}

function star_rating4(id_of_element_clicked4){
    if (id_of_element_clicked4 == '4_1star'){
        document.getElementById(id_of_element_clicked4).style.color = "Orange"
        document.getElementById('4_2star').style.color = "Black"
        document.getElementById('4_3star').style.color = "Black"
        document.getElementById('4_4star').style.color = "Black"
        document.getElementById('4_5star').style.color = "Black"
        document.getElementById('4_1star').value = 1
    }
    else if (id_of_element_clicked4 == '4_2star'){
        document.getElementById(id_of_element_clicked4).style.color = "Orange"
        document.getElementById('4_1star').style.color = "Orange"
        document.getElementById('4_3star').style.color = "Black"
        document.getElementById('4_4star').style.color = "Black"
        document.getElementById('4_5star').style.color = "Black"
        document.getElementById('4_1star').value = 2
    }
    else if (id_of_element_clicked4 == '4_3star'){
        document.getElementById(id_of_element_clicked4).style.color = "Orange"
        document.getElementById('4_2star').style.color = "Orange"
        document.getElementById('4_1star').style.color = "Orange"
        document.getElementById('4_4star').style.color = "Black"
        document.getElementById('4_5star').style.color = "Black"
        document.getElementById('4_1star').value = 3
    }
    else if (id_of_element_clicked4 == '4_4star'){
        document.getElementById(id_of_element_clicked4).style.color = "Orange"
        document.getElementById('4_3star').style.color = "Orange"
        document.getElementById('4_2star').style.color = "Orange"
        document.getElementById('4_1star').style.color = "Orange"
        document.getElementById('4_5star').style.color = "Black"
        document.getElementById('4_1star').value = 4
    }
    else if (id_of_element_clicked4 == '4_5star'){
        document.getElementById(id_of_element_clicked4).style.color = "Orange"
        document.getElementById('4_4star').style.color = "Orange"
        document.getElementById('4_3star').style.color = "Orange"
        document.getElementById('4_2star').style.color = "Orange"
        document.getElementById('4_1star').style.color = "Orange"
        document.getElementById('4_1star').value = 5
    }
}

function star_rating5(id_of_element_clicked5){
    if (id_of_element_clicked5 == '5_1star'){
        document.getElementById(id_of_element_clicked5).style.color = "Orange"
        document.getElementById('5_2star').style.color = "Black"
        document.getElementById('5_3star').style.color = "Black"
        document.getElementById('5_4star').style.color = "Black"
        document.getElementById('5_5star').style.color = "Black"
        document.getElementById('5_1star').value = 1
    }
    else if (id_of_element_clicked5 == '5_2star'){
        document.getElementById(id_of_element_clicked5).style.color = "Orange"
        document.getElementById('5_1star').style.color = "Orange"
        document.getElementById('5_3star').style.color = "Black"
        document.getElementById('5_4star').style.color = "Black"
        document.getElementById('5_5star').style.color = "Black"
        document.getElementById('5_1star').value = 2
    }
    else if (id_of_element_clicked5 == '5_3star'){
        document.getElementById(id_of_element_clicked5).style.color = "Orange"
        document.getElementById('5_2star').style.color = "Orange"
        document.getElementById('5_1star').style.color = "Orange"
        document.getElementById('5_4star').style.color = "Black"
        document.getElementById('5_5star').style.color = "Black"
        document.getElementById('5_1star').value = 3
    }
    else if (id_of_element_clicked5 == '5_4star'){
        document.getElementById(id_of_element_clicked5).style.color = "Orange"
        document.getElementById('5_3star').style.color = "Orange"
        document.getElementById('5_2star').style.color = "Orange"
        document.getElementById('5_1star').style.color = "Orange"
        document.getElementById('5_5star').style.color = "Black"
        document.getElementById('5_1star').value = 4
    }
    else if (id_of_element_clicked5 == '5_5star'){
        document.getElementById(id_of_element_clicked5).style.color = "Orange"
        document.getElementById('5_4star').style.color = "Orange"
        document.getElementById('5_3star').style.color = "Orange"
        document.getElementById('5_2star').style.color = "Orange"
        document.getElementById('5_1star').style.color = "Orange"
        document.getElementById('5_1star').value = 5
    }
}

function star_rating6(id_of_element_clicked6){
    if (id_of_element_clicked6 == '6_1star'){
        document.getElementById(id_of_element_clicked6).style.color = "Orange"
        document.getElementById('6_2star').style.color = "Black"
        document.getElementById('6_3star').style.color = "Black"
        document.getElementById('6_4star').style.color = "Black"
        document.getElementById('6_5star').style.color = "Black"
        document.getElementById('6_1star').value = 1
    }
    else if (id_of_element_clicked6 == '6_2star'){
        document.getElementById(id_of_element_clicked6).style.color = "Orange"
        document.getElementById('6_1star').style.color = "Orange"
        document.getElementById('6_3star').style.color = "Black"
        document.getElementById('6_4star').style.color = "Black"
        document.getElementById('6_5star').style.color = "Black"
        document.getElementById('6_1star').value = 2
    }
    else if (id_of_element_clicked6 == '6_3star'){
        document.getElementById(id_of_element_clicked6).style.color = "Orange"
        document.getElementById('6_2star').style.color = "Orange"
        document.getElementById('6_1star').style.color = "Orange"
        document.getElementById('6_4star').style.color = "Black"
        document.getElementById('6_5star').style.color = "Black"
        document.getElementById('6_1star').value = 3
    }
    else if (id_of_element_clicked6 == '6_4star'){
        document.getElementById(id_of_element_clicked6).style.color = "Orange"
        document.getElementById('6_3star').style.color = "Orange"
        document.getElementById('6_2star').style.color = "Orange"
        document.getElementById('6_1star').style.color = "Orange"
        document.getElementById('6_5star').style.color = "Black"
        document.getElementById('6_1star').value = 4
    }
    else if (id_of_element_clicked6 == '6_5star'){
        document.getElementById(id_of_element_clicked6).style.color = "Orange"
        document.getElementById('6_4star').style.color = "Orange"
        document.getElementById('6_3star').style.color = "Orange"
        document.getElementById('6_2star').style.color = "Orange"
        document.getElementById('6_1star').style.color = "Orange"
        document.getElementById('6_1star').value = 5
    }
}

function no(no_element_id, yes_element_id){
    document.getElementById(no_element_id).style.backgroundColor = "Orange"
    document.getElementById(no_element_id).style.color = "White"
    document.getElementById(yes_element_id).style.backgroundColor = "White"
    document.getElementById(yes_element_id).style.color = "Black"
}

function yes(yes_element_id1, no_element_id1){
    document.getElementById(yes_element_id1).style.backgroundColor = "#28a745"
    document.getElementById(yes_element_id1).style.color = "White"
    document.getElementById(no_element_id1).style.color = "Black"
    document.getElementById(no_element_id1).style.backgroundColor = "White"
}

function c1(){  //function to get checked value
    var var1 = document.getElementsByName('answer_1')
    
    for (i = 0; i < var1.length; i ++) {
        if (var1[i].checked){
            console.log(var1[i].value)       
        }
    }
}

function sub(){
    document.getElementById("feedback_form").submit()
}

function _selected_city(){
    x = document.getElementById('city').value
    document.getElementById('selected_city').value = x
}

function _station(){
    x = document.getElementById('police_station').value
    document.getElementById('station').value = x
}

function change(selected_element, value_element){
    x = document.getElementById(selected_element).value
    document.getElementById(value_element).value = x
}