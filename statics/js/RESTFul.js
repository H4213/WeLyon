function RESTful() {

    var self = this;

    this.fillResult = function(data, message, response) {
        var result = {};
        result.data = data;
        result.message = message;
        result.response = response;
        return result;
    };

    this.fillResultSucess = function(data) {
        var result = {};
        result.data = data;
        result.message = '';
        result.response = true;
        return result;
    };

    this.setup = function() {
        if (sessionStorage.getItem('user_session') !== null) {
            $.ajaxSetup({
                cache: false,
                beforeSend: function(xhr) {
                    xhr.setRequestHeader('X-Cookie', sessionStorage.getItem('user_session'));
                }
            });
        }
    };

    this.getFailMessage = function(jqXHR) {
        var message = '';
        if (jqXHR.status === 401) {
            var app = new App();
            app.logout();
            message = Messages.Login.NOT_AUTHENTICATED.description;
        } else {
            if (jqXHR.status === 400) {
                message = JSON.parse(jqXHR.responseText).descricaoErro;
            } else {
                message = Messages.RESTful.SERVER_COMMUNICATION_ERROR.description;
            }
        }
        return message;
    };

    this.insert = function(url, data, async, content_type, process_data) {
        var result = {};
        var message = '';
        try {
            $.ajax({
                type: 'POST',
                dataType: 'json',
                contentType: content_type !== undefined ? content_type : 'application/json; charset=utf-8',
                url: url,
                data: data,
                processData: process_data !== undefined ? process_data : true,
                async: async
            }).done(function(data) {
                result = self.fillResultSucess(data);
            }).fail(function(jqXHR) {
                message = self.getFailMessage(jqXHR);
                result = self.fillResult(null, message, false);
            });
        } catch (e) {
            result = self.fillResult(null, e, false);
        }
        return result;
    };

    this.update = function(url, data, async, content_type, process_data) {
        var result = {};
        var message = '';
        try {
            $.when($.ajax({
                type: 'PUT',
                dataType: 'json',
                contentType: content_type !== undefined ? content_type : 'application/json; charset=utf-8',
                url: url,
                data: data,
                processData: process_data !== undefined ? process_data : true,
                async: async
            }).done(function(data) {
                result = self.fillResultSucess(data);
            }).fail(function(jqXHR) {
                message = self.getFailMessage(jqXHR);
                result = self.fillResult(null, message, false);
            }));
        } catch (e) {
            result = self.fillResult(null, e, false);
        }
        return result;
    };

    this.delete = function(url, async) {
        var result = {};
        var message = '';
        try {
            $.ajax({
                type: 'DELETE',
                dataType: 'json',
                url: url,
                async: async
            }).done(function(data) {
                result = self.fillResultSucess(data);
            }).fail(function(jqXHR) {
                message = self.getFailMessage(jqXHR);
                result = self.fillResult(null, message, false);
            });
        } catch (e) {
            result = self.fillResult(null, e, false);
        }
        return result;
    };

    this.get = function(url, data, async) {
        var result = {};
        var message = '';
        try {
            $.ajax({
                type: 'GET',
                dataType: 'json',
                url: url,
                data: data,
                async: async
            }).done(function(data) {
                result = self.fillResultSucess(data);
            }).fail(function(jqXHR) {
                message = self.getFailMessage(jqXHR);
                result = self.fillResult(null, message, false);
            });
        } catch (e) {
            result = self.fillResult(null, e, false);
        }
        return result;
    };
}