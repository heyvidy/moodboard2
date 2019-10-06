// Fetching Moods from Backend
$.ajax({
    url: "/api/mood/",
    type: "GET",
    success: function(response) {
        for (let mood of response) {
            let myoption = `<option value=${mood.id}>${mood.emoji} ${mood.name}</option>`
            $("#moods").append(myoption)
        }
    }
});

// Fetching Actions from Backend
$.ajax({
    url: "/api/action/",
    type: "GET",
    success: function(response) {
        for (let action of response) {
            let myoption = `<option value=${action.id}>${action.emoji} ${action.name}</option>`
            $("#actions").append(myoption)
        }
    }
});

$.ajax({
    url: "/api/log/",
    type: "GET",
    success: function(response) {

        for (let log of response) {
            console.log(log)
            let card = `<div class="log-card">
                            <p>Mood: ${log.fields.mood.emoji} ${log.fields.mood.name}</p>
                            <p>Action: ${log.fields.action.emoji} ${log.fields.action.name}</p>
                            <p>Note: ${log.fields.note}</p>
                        </div>`
            $(".mood-logs").append(card)
        }
    }
});