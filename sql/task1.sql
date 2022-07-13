SELECT bid.client_number, 
    sum(if(event_value.outcome = 'win',1,0)) as 'Побед',
    sum(if(event_value.outcome = 'lose',1,0)) as 'Поражений'
FROM bid
    INNER JOIN event_entity 
        ON bid.play_id = event_entity.play_id
    INNER JOIN event_value 
        ON event_entity.play_id = event_value.play_id
GROUP BY bid.client_number;
