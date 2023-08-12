// Include the jQuery library (make sure to adjust the path to your jQuery file)
// <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

// Wait for the document to be ready
$(document).ready(function() {
  // Select the <div> element with the ID red_header using the jQuery selector
  var redHeaderDiv = $("#red_header");
  
  // Attach a click event handler to the redHeaderDiv
  redHeaderDiv.click(function() {
    // Select the <header> element using the jQuery selector
    var headerElement = $("header");
    
    // Add the class 'red' to the headerElement
    headerElement.addClass("red");
  });
});
