



// Router setup
const Foo = { template: '<div>foo</div>' }
const Bar = { template: '<div>bar</div>' }

console.log(Vue.navlist);

const routes = [
  { path: '/foo', component: Foo },
  { path: '/bar', component: Bar }
]

const router = new VueRouter({
  routes: routes
})

// eventHub: Common communication channel for components
var eventHub = new Vue()

var app = new Vue({
    el: '#application',
    router,
    data: {
        message: 'Replace this message!',
        sitesections:[
            {
                "heading":"Network"
            },{
                "heading":"Logging"
            },{
                "heading":"Device configuration"
            },{
                "heading":"Firmware & information"
            }
        ],
        networks:{
            "saved":[],
            "found":[]
        },
        config:{
            firmware: "0.1.2.3",
            settings:{
                EIC1:{
                    crc1:7,
                    crc2:8,
                    gain:9,
                    ugain:10
                },
                EIC2:{
                    crc1:1,
                    crc2:2,
                    gain:3,
                    ugain:4
                }
            }
        }
    },
    methods:{
        fetchData: function(url,callback){
            var httpRequest = new XMLHttpRequest();
            httpRequest.onreadystatechange = function(){
                if (httpRequest.readyState === XMLHttpRequest.DONE) {
                    if (httpRequest.status === 200) {
                        var response = JSON.parse(httpRequest.responseText);
                        callback(response);
                    } else {
                        //TO-DO: add alert UI for end user
                        console.log('failed to get json feed.');
                    }
                }
            }.bind(this);
            httpRequest.open('GET', url);
            httpRequest.send();
        },
        set_networks: function(response){
            
            this.networks = response;
        },
    },
    created: function(){
        this.fetchData('/networks.json', this.set_networks);
        
    },
})