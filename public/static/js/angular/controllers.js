app

.controller('MainController', ['$scope',
    function ($scope) {
        //
    }
])

.controller('Question', [
    '$scope', '$http',  
    function ($scope, $http) {
        $scope.questions = [];

        $http.get('/api/questions/')
            .success(function (data) {
                $scope.questions = data;
            })
            .error(function (error) {
                $scope.log = error.detail;
            });

        $scope.add = function () {
            var date = new Date();
            $http.post('/api/questions/', {
                question_text: $scope.question,
                pub_date: date
            }).success(function (data) {
                $scope.questions.push(data);
                $scope.question = '';
            }).error(function (error) {
                $scope.log = error.detail;
            });
        }
    }
]);