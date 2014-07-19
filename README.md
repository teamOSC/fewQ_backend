##API DOCS

+ tosc.in:8080/user_register {GET,POST:name,email,phone,profile} {RESPONSE:200/OK}
+ tosc.in:8080/customer_in {GET:email,beacon_id} {RESPONSE:token,json}
+ tosc.in:8080/customer_out {GET:email,beacon_id} {RESPONSE:token,json}
+ tosc.in:8080/feedback {GET:user_id,beacon_id,rating,comments} {RESPONSE:200/OK}
