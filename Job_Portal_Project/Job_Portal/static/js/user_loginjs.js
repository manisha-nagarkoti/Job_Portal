
   function checkpass()
   {
        var x = document.getElementById('type-of-user').value;

         if(x==1){
         alert('data gone candidate');
         window.location.href ="/user_profile";
          }

         if(x==2){
          alert('data gone recruiter');
          window.location.href ="/recuiter_login";

          }
}
