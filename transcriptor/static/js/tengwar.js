function getLanguage() {
    return $("#language").html();
}

function loadTable() {
    var posting = $.post("/table", {language: getLanguage()})
        .done(function(result) {
            $("#tengwarTable").empty().append(result);
        })
        .fail(function(xhr, status, error) {
            alert("Server error. Cannot load tengwar table!")
        });
}

function transcribe() {
    $("#loader").show();
    var language = getLanguage();
    var sourceText = $(this).val()
    var posting = $.post("/transcribe", { sourceText: sourceText, language: language})
        .done(function(result) {
            $("#loader").hide();
            $("#resultText").empty().append(result.text);
            if (language != result.language) {
                $("#detected").empty().append("[" + result.language + "]");
                $("#detected").show();
            }
            else {
                $("#detected").hide();
            }
        })
        .fail(function(xhr, status, error) {
            $("#loader").hide();
            $("#resultText").empty();
            alert("Server error. Please try again later.")
        });
}

$(document).ready(function() {

    $("#sourceText").change(transcribe);

    $("#tengwarTable").ready(loadTable);

    $("a.lang-setter").click(function () {
        var lang = $(this).html();
        if (lang === "Auto") {
            lang = null;
        }
        $("#language").empty().append(lang);
        $("#detected").hide();
        loadTable();
        return false;
    });
});

