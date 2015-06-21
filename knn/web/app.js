var ExpressMVC = require('express_mvc');
var emvc = new ExpressMVC({});
var router = new emvc.Router;
    router.addRoute('Home', 'GET', '/:age/:height/:weight', function(req, res){
        var sys = require('sys')
        var exec = require('child_process').exec;
	var cmd = "python /var/python/data-science/knn.py "+(req.query.arg || '-r')+" "+req.params.age+" "+req.params.height+" "+req.params.weight;
	console.log(cmd);
        exec(cmd, function(err, stdout, stderr){
            console.log(err, stdout, stderr);
            // python /var/python/ga/data-science/knn.py 27 182 104
            res.send(stdout);
        });
    });
    emvc.Listen(router, 9999);
