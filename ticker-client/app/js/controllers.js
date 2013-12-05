'use strict';

/* Controllers */

angular.module('myApp.controllers', []).
    controller('MyCtrl1', ['MyService', function (MyService) {
        $scope.customers = MyService.getCustomers();
    }])
    .controller('MyCtrl2', [function () {

    }]);