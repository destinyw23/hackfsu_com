/**
 * Pug build locals
 */

var moment = require('moment');

var locals = {};

locals.moment = moment;

locals.baseTitle = 'HackFSU';
locals.getTitle = function(subtitle) {
    if (subtitle && subtitle.length > 0) {
        return locals.baseTitle + ' - ' + subtitle.trim();
    }
    return locals.baseTitle;
};

locals.links = {
    twitter: 'http://www.twitter.com/HackFSU',
    facebook: 'https://www.facebook.com/hackfsu',
    instagram: 'https://www.instagram.com/hackfsu',
    github: 'https://github.com/HackFSU'
};

locals.navLinks = {
    index: [
        { name: 'REGISTER', url: '#faq' },
        { name: 'FAQ', url: '#faq' },
        { name: 'SPONSORS', url: '#sponsors' },
        { name: 'HELP', url: '#' },
        { name: 'LOGIN', url: '#' }
    ],

    // For regular non-index pages
    standard: [
        { name: 'Link 1', url: '#' },
        { name: 'Link 2', url: '#' },
        { name: 'Link 3', url: '#' },
        { name: 'Link 4', url: '#' },
        { name: 'Link 5', url: '#' }
    ]
};

module.exports = locals;
