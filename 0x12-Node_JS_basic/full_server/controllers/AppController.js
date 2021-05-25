class AppController {
  static getHomePage(request, response) {
    return response.status(200).send('Hello Holberton School!');
  }
}

module.exports = AppController;
