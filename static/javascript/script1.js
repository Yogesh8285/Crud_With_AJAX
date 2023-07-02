
// Edit Employee code
// function Edit(id,ename,email,dob,gender,education,password)
// {
//     document.getElementById("id").value = id;
//     document.getElementById("ename").value = ename;
//     document.getElementById("email").value = email;
//     document.getElementById("dob").value = dob;
//     document.getElementById("education").value = education;
//     document.getElementById("pass").value = password ;
//     document.getElementById("gender").value = gender ;
//     alert(gender);
//     if(gender == 'Male')
//         {document.getElementById("gender_Male").checked = true;}
//     else
//         {document.getElementById("gender_female").checked = true;}

    
    // var x = document.getElementById("pass");
    // if (document.getElementById("pass").type == "password") {
    //     x.type = "text";}
// }


// Remove employee confirm code
function Remove(myid)
    {
        document.getElementById("myid").value = myid;
    }

// Password visible code

function visible()
    {
        var x = document.getElementById("pass");
        if (document.getElementById("pass").type == "password") 
        {
            x.type = "text";
        }
        else{
            x.type = "password"
        }
 }
