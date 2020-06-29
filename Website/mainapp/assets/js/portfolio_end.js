var slideIndex = 1;
	  showSlides(slideIndex);
	function plusSlides(n) {
	  showSlides(slideIndex += n);
	}
	function currentSlide(n) {
	  showSlides(slideIndex = n);
	}
	function showSlides(n) {
	  var i;
	  var slides = document.getElementsByClassName("mySlides");
	  var dots = document.getElementsByClassName("dot");
		if (n > slides.length) {slideIndex = 1}    
		if (n < 1) {slideIndex = slides.length}
		  for (i = 0; i < slides.length; i++) {
		  slides[i].style.display = "none";  
		  }
		  for (i = 0; i < dots.length; i++) {
			dots[i].className = dots[i].className.replace(" active", "");
		  }
	  slides[slideIndex-1].style.display = "block";  
	  dots[slideIndex-1].className += " active";
	}

$(".ContactForm").on('submit', function(e){
	e.preventDefault();

	var serializedData = $(this).serialize();
	$.ajax({
		type:'POST',
		url:"{% url 'createContact' %}",
		data: serializedData,
		csrfmiddlewaretoken: '{{ csrf_token }}',
		dataType: 'json',
		success:function(){
			alert("Thank you and I look forward to connecting with you!");
		},
		error:function(response){
			alert(response["responseJSON"]["error"]);
		}
	});
});
	  
	