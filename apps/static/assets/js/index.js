
const app = new Vue({
  data:{
    eventlist: eventlist,
    comeventlist: comeventlist
  },
  components:{
    "getchart": {
      template:
        "<div>"+
          "<div>{{ this.message }}</div>"+
          "<div>{{ convertjson() }}</div>"+
        "</div>",
      props:{
        eventlist: {},
        comeventlist: {}
      },
      data(){
        return{
        }
      },
      methods:{
        convertjson: function(){
          console.log("work");
          console.log(this.eventlist);
          a = this.eventlist.replace(/&#x27;/g,'').replace(/<QuerySet /, '').replace(/>/, '').replace(/datetime.date/g, '').replace(/\(/g, "[" ).replace(/\)/g,"]").replace(/'/g, '"')
          b = this.comeventlist.replace(/&#x27;/g,'').replace(/<QuerySet /, '').replace(/>/, '').replace(/datetime.date/g, '').replace(/\(/g, "[" ).replace(/\)/g,"]").replace(/'/g, '"')
          console.log(a)
          eventlistjson = JSON.parse(a)
          comeventlistjson = JSON.parse(b)
          console.log(eventlistjson)
          console.log(comeventlistjson)
          
        }
      }
    }
  }
});

app.$mount("#chartBig1");