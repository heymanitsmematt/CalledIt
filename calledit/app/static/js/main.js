$(document).ready(function() { 
    $(document).tableXHR()
    
    var calledIt = calledIt || {};

    //ns.main = function() {
//	    return;	
//	}
});

$.fn.extend({ 
    tableXHR : function() { 
        $('.sportRow').click(function(event) {
	    tgt = event.originalEvent.currentTarget   
	    if ($._data(tgt, 'teams') == undefined){
	        $._data(event.originalEvent.currentTarget, 'teams', $(tgt).find('td'))
	        $.get('/api/getSportTeams/?sport='+encodeURIComponent($.trim($(this).text())), function(data){
		    $._data($('.activeSport'), 'teams', $('.activeSport').find('td'))
		    $('.activeSport').find('tr').detach().end().removeClass('activeSport')	
	            $(tgt).addClass('activeSport');
		    pushTableUpdates(data)
	        })
	    }
	    else {
		teams = $._data(tgt, 'teams')
		$(teams).appendTo(tgt.id)
	    };

	});
    },
});

function pushTableUpdates(data) {
    teams = JSON.parse(data)
    rows = ''
    for (var i=0; i<teams.length; i++){
	team = teams[i]
	thisRow = '<tr><td id="addedRow">'+team.fields.teamName+'</td></tr>'
	rows+=thisRow
    };
    return $(rows).appendTo('.activeSport')
};
