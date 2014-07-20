##API DOCS

+ tosc.in:8080/user_register {GET,POST:name,email,phone,profile} {RESPONSE:200/OK}
+ tosc.in:8080/customer_in {GET:email,beacon_id} {RESPONSE:token,json}
+ tosc.in:8080/customer_out {GET:email,beacon_id} {RESPONSE:token,json}
+ tosc.in:8080/feedback {GET:email,beacon_id,rating,comments} {RESPONSE:200/OK}
+ tosc.in:8080/search {GET:email} {RESPONSE: <json>}
+ tosc.in:8080/transaction {GET:email,order} {RESPONSE: 200}
