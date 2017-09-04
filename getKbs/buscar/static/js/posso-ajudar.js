
	document.getElementById('here').innerHTML = "<a href='#' onclick='MyFunction()' id='#myBtn'> Posso Ajudar? </a> ";

    	$("#here").click(function (event) {
    event.preventDefault();
    $('<div></div>')
        .html('<iframe style="border: 0px; " src="http://possoteajudar.cloud.globoi.com/index.html" width="100%" height="100%"></iframe>')
        .dialog({
            autoOpen: true,
            modal: true,
            height: 500,
            width: 400,
            title: "Posso te ajudar?"
    });
});

    


    



 