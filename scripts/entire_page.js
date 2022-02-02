var page = require('webpage').create();
system = require('system'),
url = system.args[1];
page.open(url, function() {
    setTimeout(function() {
    //viewportSize being the actual size of the headless browser
    page.viewportSize = { width: 1024, height: 768 };
    //the clipRect is the portion of the page you are taking a screenshot of
    //page.clipRect = { top: 0, left: 0, width: 1024, height: 768 };
        page.render('google.png');
        phantom.exit();
    }, 200);
});