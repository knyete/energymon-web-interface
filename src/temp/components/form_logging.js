'use strict';

Vue.component('form-logging', {
    data: function data() {
        return {
            service: '-- No service selected --',
            ts_APIkey: '',
            aws_subdomain: '',
            aws_region: ''
        };
    },
    template: '\n        <form id="form form__logging">\n            <p>\n                <label>\n                    Logging service\n                    <select v-model="service">\n                        <option>-- No service selected --</option>\n                        <option>ThingSpeak</option>\n                        <option>AWS IoT</option>\n                    </select>\n                </label>\n            </p>\n            \n            <p v-if="service==\'ThingSpeak\'">\n                <label>\n                    API Key <input type="text" v-model="ts_APIkey">\n                </label>\n            </p>\n            <template v-if="service==\'AWS IoT\'">\n                <p>\n                    <label>\n                        Certificate <input type="file">\n                    </label>\n                </p>\n                <p>\n                    <label>\n                        Private key <input type="file">\n                    </label>\n                </p>\n                <p>\n                    <label>\n                        Endpoint subdomain <input type="text" v-model="aws_subdomain">\n                    </label>\n                </p>\n                <p>\n                    <label>\n                        Endpoint region <input type="text" v-model="aws_region">\n                    </label>\n                </p>\n            </template>\n            <p><button>Cancel</button> <button>Save</button></p>\n        </form>\n    '
});