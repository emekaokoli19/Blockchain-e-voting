function validate(){
    const password1 = document.getElementById("id_password").value
    const password2 = document.getElementById("id_confirm_password").value
    const PVC_no = document.getElementById("id_PVC_no").value
    var error = document.getElementById("error")
    const click = document.getElementById("button")
    var message
    click.addEventListener('click', function(event){
        event.preventDefault()
    })
    /*if (password1 != password2){
        message = "Passwords must match"
        error.style.padding = "20px"
        error.innerHTML = message
        return false 
    }
    else if(PVC_no.length < 5){
        message = "PVC number must be more than 5 digits"
        error.style.padding = "20px"
        error.innerHTML = message
        return false
    }
    else{return true}*/
}

function check(){
    var count = 0
    const n = document.getElementById("check")
    n.addEventListener('click', function(e){
        count = count + 1
    })
    console.log(count)
}

