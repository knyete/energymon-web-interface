# Autogenerated file
def render(logging_services, active_logger):
    yield """

<!DOCTYPE html>
<html lang=\"en\">
    """
# Autogenerated file
    def render1(*a, **d):
        yield """ <head>
    <meta charset=\"utf-8\">
    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
    <link rel=\"stylesheet\" type=\"text/css\" href=\"/static/styles.css\" />
    <title>Whatnick: Energy Monitor</title>
</head>"""
    yield from render1()
    yield """
	<body>
       """
# Autogenerated file
    def render2(*a, **d):
        yield """<div class=\"masthead\">
    <svg width=\"86.492px\" height=\"76.729px\">
    <g>
        <path fill=\"#858A8E\" d=\"M20.703,23.669c-0.677-0.449-1.459-0.671-2.344-0.671c-0.948,0-1.834,0.262-2.656,0.783
            c-0.823,0.521-1.508,1.286-2.057,2.291c-0.259-0.753-0.565-1.334-0.918-1.737c-0.354-0.403-0.811-0.728-1.369-0.971
            c-0.559-0.245-1.147-0.366-1.769-0.366c-0.919,0-1.797,0.253-2.63,0.752c-0.604,0.379-1.195,0.976-1.769,1.793v-2.215
            c0-0.456-0.368-0.824-0.824-0.824s-0.825,0.368-0.825,0.824v12.319c0,0.456,0.369,0.825,0.825,0.825s0.824-0.369,0.824-0.825
            v-4.935c0-1.602,0.159-2.791,0.478-3.569c0.318-0.776,0.809-1.395,1.471-1.854C7.804,24.83,8.518,24.6,9.279,24.6
            c0.66,0,1.23,0.167,1.708,0.501c0.478,0.333,0.815,0.778,1.007,1.331c0.192,0.554,0.289,1.604,0.289,3.15v6.065
            c0,0.456,0.368,0.825,0.824,0.825c0.456,0,0.824-0.369,0.824-0.825v-4.522c0-1.837,0.153-3.149,0.457-3.934
            c0.307-0.786,0.79-1.414,1.452-1.885c0.661-0.472,1.389-0.707,2.188-0.707c0.658,0,1.223,0.157,1.696,0.472
            c0.474,0.314,0.808,0.728,1.004,1.242c0.196,0.515,0.293,1.457,0.293,2.833v6.501h0.035c0,0.456,0.369,0.825,0.824,0.825
            c0.456,0,0.825-0.369,0.825-0.825v-6.501c0-1.602-0.165-2.804-0.493-3.604C21.884,24.741,21.38,24.118,20.703,23.669z\"/>
        <path fill=\"#858A8E\" d=\"M31.04,22.998c-1.982,0-3.623,0.719-4.92,2.156c-1.179,1.303-1.769,2.84-1.769,4.616
            c0,1.79,0.623,3.354,1.87,4.693c1.246,1.339,2.854,2.009,4.819,2.009c1.959,0,3.563-0.67,4.808-2.009
            c1.247-1.339,1.871-2.903,1.871-4.693c0-1.781-0.59-3.325-1.769-4.629C34.651,23.712,33.014,22.998,31.04,22.998z M35.372,32.397
            c-0.45,0.8-1.055,1.419-1.821,1.855c-0.763,0.435-1.602,0.652-2.517,0.652c-0.914,0-1.753-0.218-2.516-0.652
            c-0.766-0.437-1.372-1.056-1.821-1.855c-0.451-0.801-0.673-1.665-0.673-2.591c0-1.438,0.492-2.663,1.477-3.676
            c0.985-1.013,2.164-1.52,3.534-1.52c1.363,0,2.54,0.507,3.528,1.52c0.99,1.013,1.484,2.237,1.484,3.676
            C36.046,30.732,35.821,31.597,35.372,32.397z\"/>
        <path fill=\"#858A8E\" d=\"M48.567,23.729c-0.742-0.486-1.59-0.73-2.549-0.73c-0.943,0-1.815,0.219-2.615,0.654
            c-0.801,0.435-1.531,1.093-2.191,1.973v-2.297c0-0.456-0.369-0.824-0.824-0.824c-0.457,0-0.824,0.368-0.824,0.824v12.319
            c0,0.456,0.368,0.825,0.824,0.825c0.456,0,0.824-0.369,0.824-0.825v-4.204c0-1.688,0.077-2.851,0.236-3.486
            c0.251-0.976,0.771-1.79,1.56-2.45c0.79-0.66,1.683-0.989,2.679-0.989c0.872,0,1.579,0.213,2.122,0.642
            c0.541,0.428,0.908,1.066,1.098,1.914c0.123,0.494,0.185,1.48,0.185,2.956v5.618c0,0.456,0.368,0.825,0.824,0.825
            s0.825-0.369,0.825-0.825v-6.1c0-1.744-0.178-3.028-0.531-3.853S49.309,24.215,48.567,23.729z\"/>
        <path fill=\"#858A8E\" d=\"M53.639,18.051c-0.368,0-0.685,0.134-0.951,0.4c-0.265,0.268-0.397,0.59-0.397,0.966
            c0,0.368,0.133,0.687,0.397,0.955c0.267,0.266,0.583,0.399,0.951,0.399c0.375,0,0.695-0.134,0.963-0.399
            C54.866,20.104,55,19.785,55,19.417c0-0.376-0.134-0.698-0.397-0.966C54.334,18.185,54.014,18.051,53.639,18.051z\"/>
        <path fill=\"#858A8E\" d=\"M69.725,22.998c-1.983,0-3.624,0.719-4.922,2.156c-1.179,1.303-1.77,2.84-1.77,4.616
            c0,1.79,0.623,3.354,1.871,4.693c1.246,1.339,2.854,2.009,4.82,2.009c1.957,0,3.561-0.67,4.807-2.009
            c1.247-1.339,1.871-2.903,1.871-4.693c0-1.781-0.59-3.325-1.77-4.629C73.334,23.712,71.698,22.998,69.725,22.998z M74.055,32.397
            c-0.449,0.8-1.054,1.419-1.82,1.855c-0.763,0.435-1.604,0.652-2.518,0.652s-1.753-0.218-2.516-0.652
            c-0.766-0.437-1.371-1.056-1.821-1.855c-0.45-0.801-0.675-1.665-0.675-2.591c0-1.438,0.494-2.663,1.479-3.676
            s2.163-1.52,3.533-1.52c1.365,0,2.54,0.507,3.529,1.52c0.988,1.013,1.484,2.237,1.484,3.676
            C74.731,30.732,74.504,31.597,74.055,32.397z\"/>
        <path fill=\"#858A8E\" d=\"M53.645,23.328c-0.456,0-0.826,0.367-0.826,0.824v11.495c0,0.456,0.37,0.825,0.826,0.825
            s0.824-0.369,0.824-0.825V24.152C54.469,23.695,54.101,23.328,53.645,23.328z\"/>
        <path fill=\"#858A8E\" d=\"M61.867,23.328h-2.091v-3.295c0.129,0.053,0.254,0.108,0.392,0.157c0.876,0.311,1.864,0.465,2.962,0.465
            c1.5,0,2.783-0.316,3.852-0.953c1.068-0.636,1.818-1.543,2.25-2.721c0.314-0.831,0.471-2.148,0.471-3.946V2.824
            C69.702,2.369,69.333,2,68.877,2s-0.824,0.369-0.824,0.824v2.227c-0.771-0.911-1.57-1.564-2.399-1.961
            c-0.829-0.398-1.724-0.596-2.683-0.596c-1.154,0-2.254,0.299-3.295,0.895c-1.043,0.598-1.857,1.408-2.446,2.433
            c-0.59,1.025-0.885,2.131-0.885,3.316s0.282,2.272,0.849,3.263c0.566,0.989,1.367,1.776,2.406,2.361
            c1.036,0.586,2.146,0.878,3.324,0.878c1.006,0,1.957-0.211,2.854-0.631c0.896-0.419,1.654-1.022,2.275-1.808v0.659
            c0,1.411-0.165,2.437-0.496,3.07c-0.33,0.633-0.881,1.159-1.656,1.58c-0.775,0.418-1.725,0.626-2.848,0.626
            c-1.141,0-2.096-0.202-2.865-0.612c-0.236-0.125-0.455-0.277-0.664-0.442c-0.041-0.041-0.088-0.075-0.136-0.105
            c-0.003-0.001-0.005-0.004-0.007-0.005c0,0,0,0-0.001,0c-0.125-0.076-0.271-0.121-0.429-0.121c-0.455,0-0.824,0.368-0.824,0.823
            v4.654h-1.782c-0.394,0-0.714,0.319-0.714,0.712c0,0.395,0.32,0.713,0.714,0.713h1.782v10.895c0,0.456,0.369,0.825,0.824,0.825
            c0.456,0,0.824-0.369,0.824-0.825V24.753h2.091c0.394,0,0.714-0.318,0.714-0.713C62.581,23.647,62.26,23.328,61.867,23.328z
             M66.751,12.719c-0.924,0.908-2.142,1.365-3.657,1.365c-1.499,0-2.721-0.46-3.662-1.377c-0.943-0.919-1.414-2.082-1.414-3.487
            c0-0.927,0.227-1.786,0.683-2.585c0.456-0.797,1.083-1.421,1.886-1.873c0.8-0.449,1.668-0.677,2.602-0.677
            c0.896,0,1.731,0.219,2.51,0.658c0.776,0.441,1.378,1.039,1.801,1.798c0.425,0.757,0.637,1.619,0.637,2.585
            C68.135,10.61,67.675,11.807,66.751,12.719z\"/>
        <path fill=\"#858A8E\" d=\"M84.1,23.435c-0.518-0.292-1.005-0.437-1.461-0.437c-0.605,0-1.184,0.183-1.742,0.546
            c-0.559,0.368-1.089,0.917-1.59,1.657v-1.873c0-0.466-0.377-0.842-0.843-0.842c-0.467,0-0.843,0.376-0.843,0.842v12.319
            c0,0.465,0.377,0.843,0.843,0.843s0.843-0.378,0.843-0.843v-3.839c0-2.223,0.101-3.699,0.307-4.429
            c0.266-0.952,0.653-1.651,1.166-2.103c0.51-0.451,1.041-0.678,1.59-0.678c0.227,0,0.507,0.074,0.838,0.213
            c0.01,0.006,0.014,0.018,0.025,0.022c0.389,0.241,0.895,0.122,1.135-0.267C84.609,24.182,84.489,23.673,84.1,23.435z\"/>
        <path fill=\"#858A8E\" d=\"M8.672,15.969c0.943,0,1.788-0.143,2.535-0.43c0.746-0.285,1.419-0.706,2.017-1.254
            c0.597-0.551,1.124-1.272,1.579-2.168l-0.009-0.005c0.053-0.104,0.089-0.219,0.089-0.345c0-0.432-0.348-0.779-0.779-0.779
            c-0.293,0-0.54,0.169-0.672,0.409l-0.018-0.011c-0.503,0.837-0.97,1.442-1.404,1.819c-0.433,0.376-0.957,0.677-1.574,0.903
            c-0.617,0.228-1.252,0.34-1.904,0.34c-1.352,0-2.489-0.476-3.407-1.429c-0.922-0.95-1.398-2.171-1.428-3.659h11.531
            c-0.016-1.751-0.488-3.212-1.414-4.381c-1.306-1.657-3.049-2.486-5.234-2.486c-2.121,0-3.815,0.81-5.082,2.427
            C2.5,6.193,2,7.642,2,9.267c0,1.728,0.588,3.278,1.77,4.646C4.947,15.284,6.582,15.969,8.672,15.969z M5.359,5.286
            c0.904-0.809,1.985-1.214,3.243-1.214c0.761,0,1.489,0.163,2.181,0.483c0.692,0.323,1.247,0.746,1.669,1.272
            c0.42,0.527,0.74,1.229,0.961,2.107H3.861C4.199,6.759,4.698,5.875,5.359,5.286z\"/>
        <path fill=\"#858A8E\" d=\"M19.391,15.969c0.456,0,0.825-0.369,0.825-0.823V10.94c0-1.689,0.078-2.851,0.236-3.487
            c0.25-0.976,0.77-1.79,1.559-2.45c0.789-0.66,1.684-0.989,2.681-0.989c0.872,0,1.578,0.214,2.12,0.643
            c0.542,0.428,0.909,1.066,1.1,1.913c0.123,0.495,0.184,1.482,0.184,2.957v5.619c0,0.454,0.368,0.823,0.824,0.823
            c0.457,0,0.825-0.369,0.825-0.823V9.044c0-1.744-0.177-3.027-0.53-3.853C28.86,4.368,28.313,3.71,27.57,3.225
            c-0.742-0.486-1.591-0.73-2.549-0.73c-0.941,0-1.813,0.219-2.614,0.654s-1.531,1.092-2.191,1.973V2.824
            C20.216,2.369,19.847,2,19.391,2c-0.455,0-0.824,0.369-0.824,0.824v12.321C18.567,15.6,18.936,15.969,19.391,15.969z\"/>
        <path fill=\"#858A8E\" d=\"M39.591,15.969c0.942,0,1.789-0.143,2.535-0.43c0.746-0.285,1.418-0.706,2.015-1.254
            c0.585-0.541,1.102-1.25,1.551-2.12c0.072-0.118,0.123-0.249,0.123-0.397c0-0.432-0.349-0.779-0.779-0.779
            c-0.297,0-0.546,0.17-0.677,0.414l-0.029-0.016c-0.501,0.837-0.97,1.442-1.402,1.819c-0.433,0.376-0.958,0.677-1.574,0.903
            c-0.617,0.228-1.252,0.34-1.904,0.34c-1.353,0-2.488-0.476-3.409-1.429c-0.919-0.95-1.396-2.171-1.427-3.659h11.531
            c-0.016-1.751-0.487-3.212-1.414-4.381c-1.305-1.657-3.051-2.486-5.234-2.486c-2.123,0-3.816,0.81-5.082,2.427
            c-0.999,1.272-1.499,2.721-1.499,4.346c0,1.728,0.591,3.278,1.77,4.646C35.866,15.284,37.499,15.969,39.591,15.969z M36.277,5.286
            c0.904-0.809,1.985-1.214,3.244-1.214c0.761,0,1.488,0.163,2.181,0.483c0.691,0.323,1.248,0.746,1.668,1.272
            c0.422,0.527,0.742,1.229,0.961,2.107h-9.552C35.118,6.759,35.617,5.875,36.277,5.286z\"/>
        <path fill=\"#858A8E\" d=\"M84.032,3.337c0.092-0.366-0.076-0.758-0.434-0.917c-0.402-0.179-0.873,0.003-1.053,0.403
            c0,0.001,0,0.001,0,0.002l-4.275,9.867l-4.405-9.868c-0.179-0.401-0.649-0.581-1.051-0.401c-0.403,0.18-0.583,0.648-0.403,1.051
            l4.973,11.194l-2.182,5.01c-0.18,0.401,0.002,0.873,0.401,1.051c0.403,0.18,0.872-0.001,1.054-0.401L84.071,3.35L84.032,3.337z\"/>
        <path fill=\"#858A8E\" d=\"M55.315,2.968l0.023-0.037c-0.518-0.291-1.006-0.437-1.461-0.437c-0.605,0-1.186,0.183-1.742,0.548
            c-0.559,0.366-1.089,0.917-1.59,1.655V2.824h-0.018C50.528,2.369,50.16,2,49.704,2c-0.455,0-0.824,0.369-0.824,0.824h-0.019v12.321
            h0.019c0,0.454,0.369,0.823,0.824,0.823c0.456,0,0.824-0.369,0.824-0.823h0.018v-3.841c0-2.222,0.1-3.699,0.305-4.428
            c0.268-0.951,0.656-1.651,1.167-2.103c0.511-0.452,1.04-0.678,1.59-0.678c0.208,0,0.466,0.068,0.761,0.185
            c0.141,0.115,0.313,0.191,0.51,0.191c0.456,0,0.824-0.368,0.824-0.824C55.702,3.356,55.543,3.113,55.315,2.968z\"/>
    </g>
    <g>
        <path fill=\"#CCFF00\" d=\"M45.948,36.544c0.148-1.682,1.645-2.936,3.326-2.79l0,0c1.682,0.147,2.938,1.644,2.791,3.327l-2.613,29.877
            c-0.148,1.682-1.645,2.937-3.326,2.791l0,0c-1.682-0.148-2.938-1.644-2.791-3.326L45.948,36.544z\"/>
        <path fill=\"#CCFF00\" d=\"M37.041,41.513c0.147-1.682,1.643-2.938,3.325-2.791l0,0c1.683,0.148,2.938,1.644,2.791,3.326
            l-2.615,29.879c-0.146,1.682-1.642,2.936-3.324,2.79l0,0c-1.682-0.148-2.938-1.644-2.791-3.327L37.041,41.513z\"/>
        <path fill=\"#CCFF00\" d=\"M16.436,56.927c-0.147,1.682-1.643,2.937-3.326,2.789l0,0c-1.682-0.146-2.937-1.642-2.79-3.324l0,0
            c0.147-1.683,1.643-2.938,3.325-2.791l0,0C15.328,53.748,16.582,55.244,16.436,56.927L16.436,56.927z\"/>
        <path fill=\"#CCFF00\" d=\"M25.061,55.194c-0.147,1.682-1.645,2.937-3.326,2.789l0,0c-1.681-0.146-2.938-1.644-2.79-3.324l0.294-3.373
            c0.148-1.681,1.645-2.936,3.326-2.79l0,0c1.682,0.147,2.938,1.644,2.79,3.326L25.061,55.194z\"/>
        <path fill=\"#CCFF00\" d=\"M33.659,53.766c-0.147,1.682-1.644,2.937-3.326,2.791l0,0c-1.682-0.147-2.938-1.644-2.791-3.326l0.591-6.75
            c0.147-1.681,1.644-2.937,3.325-2.789l0,0c1.682,0.146,2.937,1.643,2.791,3.324L33.659,53.766z\"/>
        <path fill=\"#CCFF00\" d=\"M70.057,51.544c0.146-1.682,1.643-2.937,3.324-2.789l0,0c1.683,0.146,2.938,1.642,2.791,3.324l0,0
            c-0.147,1.683-1.645,2.938-3.326,2.791l0,0C71.165,54.723,69.909,53.227,70.057,51.544L70.057,51.544z\"/>
        <path fill=\"#CCFF00\" d=\"M61.432,53.276c0.146-1.682,1.643-2.937,3.324-2.789l0,0c1.683,0.146,2.938,1.644,2.791,3.324l-0.296,3.373
            c-0.146,1.681-1.643,2.937-3.324,2.79l0,0c-1.683-0.147-2.937-1.644-2.791-3.326L61.432,53.276z\"/>
        <path fill=\"#CCFF00\" d=\"M52.834,54.705c0.146-1.682,1.642-2.937,3.324-2.791l0,0c1.682,0.147,2.936,1.644,2.79,3.326l-0.59,6.75
            c-0.147,1.681-1.644,2.937-3.326,2.789l0,0c-1.683-0.146-2.938-1.643-2.79-3.324L52.834,54.705z\"/>
    </g>
    </svg>
</div>"""
    yield from render2()
    yield """
        <div id=\"vue_app\" class=\"pagesection\">
            <div  v-cloak  class=\"component\">
                <div class=\"ui__header\">
                    <h1>Logging service</h1>
                </div>
                <div class=\"ui__body\">
                    <form class=\"form form__logging\">
                        <fieldset>
                            <p>
                                <label>
                                    Logging service
                                    <select v-model=\"service\">
                                        <option>-- No service selected --</option>
                                        """
    for service in logging_services:
        yield """
                                        <option"""
        if service.name == active_logger:
            yield """ selected"""
        yield """>"""
        yield str(service.name)
        yield """</option>
                                        """
    yield """
                                    </select>
                                </label>
                            </p>
                        </fieldset>
                        <fieldset v-if=\"service=='ThingSpeak'\">
                        <h3>ThingSpeak</h3>
                            <p>
                                <label>
                                    API Key <input type=\"text\" v-model=\"ts.key\">
                                </label>
                            </p>
                        </fieldset>
                        <fieldset v-if=\"service=='AWS IoT'\">
                        <h3>Amazon web service, IoT</h3>
                            <p>
                                <label>
                                    Certificate <input type=\"file\">
                                </label>
                            </p>
                            <p>
                                <label>
                                    Private key <input type=\"file\">
                                </label>
                            </p>
                            <p>
                                <label>
                                    Endpoint subdomain <input type=\"text\" v-model=\"awsiot.subdomain\">
                                </label>
                            </p>
                            <p>
                                <label>
                                    Endpoint region <input type=\"text\" v-model=\"awsiot.region\">
                                </label>
                            </p>
                        </fieldset>
                        <p>
                            <a class=\"button\" href=\"/\">Cancel</a> 
                            <button>Save</button>
                        </p>
                    </form>
                </div>
            </div>
        </div>
        """
# Autogenerated file
    def render3(*a, **d):
        yield """<script src=\"/static/vendor/vue_development.js\"></script>"""
    yield from render3()
    yield """
        <script>
            var app = new Vue("""
    yield """{
                el: '#vue_app',
                data: """
    yield """{
                    service :\""""
    yield str(active_logger)
    yield """\",
                    ts:"""
    yield """{
                        key  : ''              
                    },
                    awsiot:"""
    yield """{
                        cert  : '',
                        key  : '',
                        subdomain: '',
                        region: ''   
                    }
                },
                 computed:"""
    yield """{
                    formValid: function()"""
    yield """{
                        if(this.service != \"-- No service selected --\")"""
    yield """{
                            return true;
                        }
                        return false;
                    },
                }
            })
        </script>
	</body>
</html>"""
