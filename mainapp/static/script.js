function updateValue(){
    data={
        'date':document.getElementById("date").value,
    }
    setRequestHeader();

    $.ajax({
        dataType: 'json',
        type: 'POST',
        url: "/predict/",
        data: data,
        success: function (data) {
            console.log("Success:", data);
            document.getElementById("result_model").innerHTML = "$"+data.predicted_price;
        },
        error: function (jqXHR, textStatus, errorThrown) {
            console.log("Error:", jqXHR);
            alert("updated failed!! ")
        }
    });
}




// Function to GET csrftoken from Cookie
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');




function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

// Function to set Request Header with `CSRFTOKEN`
function setRequestHeader(){
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
}