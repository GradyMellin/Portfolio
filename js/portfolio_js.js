
$(document).ready(function(){   
    $("a").on('click', function(event) {
        
      // Make sure this.Link has a value before overriding default behavior
      if (this.Link !== "") {
        // Prevent default anchor click behavior
        event.preventDefault();
  
        // Store Link
        var Link = this.Link;
  
        // Using jQuery's animate() method to add smooth page scroll
        // The optional number (2000) specifies the number of milliseconds it takes to scroll to the specified area
        $('html, body').animate({
          scrollTop: $(Link).offset().top
        }, 2000, function(){
     
          // Add Link (#) to URL when done scrolling (default click behavior)
          window.location.Link = Link;
        });
      } // End if
    });
  });

function openForm() {
    $("#myForm").slideDown();( "slow" );
  }
  
  function closeForm() {
    $("#myForm").slideUp();( "slow" );
  }
