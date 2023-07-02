<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
// Remove employee

// $("tbody").on("click", ".btn-del",function(){
    $("#remove-emp").click(function(){
        console.log("Delete click");
        output = ''
        var id = $('#myid').val()
        var csr = $("input[name=csrfmiddlewaretoken").val();
        console.log(id);
        mydata = {empid : id,csrfmiddlewaretoken:csr};
        $.ajax({
          url :"{% url 'Remove'%}",
          method :"POST",
          data :mydata,
          dataType:'json',
          success: function(data){
            console.log(data.employee);
            if (data.status == "save"){
                  x = data.employee;
                  console.log("From submited");
                  for (i=0; i<x.length; i++){
                    output += "<tr><td>"+(i+1)+
                      "</td><td>"+x[i].id +
                        "</td><td>"+x[i].ename+
                        "</td><td>"+x[i].email+
                        "</td><td>"+x[i].Birth_date+
                        "</td><td>"+x[i].education+
                        "</td><td>"+x[i].gender+
                        "</td><td>"+x[i].password+
                        "</td><td><button type='button'style='margin: 5px;' class='btn btn-primary btn-sm' data-bs-toggle='modal' data-bs-target='#EditModal' value='Edit' onclick='editcall("+x[i].id+")>"+'Edit'+"</button>'"+ 
                        "</td><td><button type='button' class='btn btn-danger btn-sm btn-del' data-bs-toggle='modal' data-bs-target='#remove' value='Remove' onclick='Remove("+x[i].id+")>"+'Remove'+"</button>'>"
      
                      
                  }
                  $("#tbody").html(output);
          }
        }
        })
      })