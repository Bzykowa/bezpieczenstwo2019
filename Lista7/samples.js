var mime_samples = [
  { 'mime': 'application/xhtml+xml', 'samples': [
    { 'url': 'http://127.0.0.1:7000/', 'dir': '_m0/0', 'linked': 2, 'len': 472 },
    { 'url': 'http://127.0.0.1:7000/accounts/', 'dir': '_m0/1', 'linked': 2, 'len': 4385 },
    { 'url': 'http://127.0.0.1:7000/admin/login/', 'dir': '_m0/2', 'linked': 5, 'len': 1903 },
    { 'url': 'http://127.0.0.1:7000/static/', 'dir': '_m0/3', 'linked': 2, 'len': 1634 } ]
  },
  { 'mime': 'text/css', 'samples': [
    { 'url': 'http://127.0.0.1:7000/static/style.css/', 'dir': '_m1/0', 'linked': 2, 'len': 608 } ]
  }
];

var issue_samples = [
  { 'severity': 3, 'type': 40601, 'samples': [
    { 'url': 'http://127.0.0.1:7000/', 'extra': 'implicitly cacheable \x27Set-Cookie\x27 response', 'sid': '0', 'dir': '_i0/0' } ]
  },
  { 'severity': 3, 'type': 40402, 'samples': [
    { 'url': 'http://127.0.0.1:7000/', 'extra': 'Python error', 'sid': '22004', 'dir': '_i1/0' },
    { 'url': 'http://127.0.0.1:7000/admin/', 'extra': 'Python error', 'sid': '22004', 'dir': '_i1/1' },
    { 'url': 'http://127.0.0.1:7000/admin/logout/', 'extra': 'Python error', 'sid': '22004', 'dir': '_i1/2' } ]
  },
  { 'severity': 1, 'type': 20102, 'samples': [
    { 'url': 'http://127.0.0.1:7000/advertise.sfish', 'extra': 'Too many previous fetch failures', 'sid': '0', 'dir': '_i2/0' },
    { 'url': 'http://127.0.0.1:7000/accounts/', 'extra': 'Too many previous fetch failures', 'sid': '0', 'dir': '_i2/1' },
    { 'url': 'http://127.0.0.1:7000/sfi9876/logout/', 'extra': 'Too many previous fetch failures', 'sid': '0', 'dir': '_i2/2' },
    { 'url': 'http://127.0.0.1:7000/admin/recycled.sfish', 'extra': 'Too many previous fetch failures', 'sid': '0', 'dir': '_i2/3' },
    { 'url': 'http://127.0.0.1:7000/sfi9876/login/', 'extra': 'Too many previous fetch failures', 'sid': '0', 'dir': '_i2/4' },
    { 'url': 'http://127.0.0.1:7000/admin/login/', 'extra': 'Too many previous fetch failures', 'sid': '0', 'dir': '_i2/5' },
    { 'url': 'http://127.0.0.1:7000/admin/login/?next=/admin/', 'extra': 'Too many previous fetch failures', 'sid': '0', 'dir': '_i2/6' },
    { 'url': 'http://127.0.0.1:7000/admin/login/', 'extra': 'Too many previous fetch failures', 'sid': '0', 'dir': '_i2/7' },
    { 'url': 'http://127.0.0.1:7000/admin/login/', 'extra': 'Too many previous fetch failures', 'sid': '0', 'dir': '_i2/8' },
    { 'url': 'http://127.0.0.1:7000/static/--\x3e\x22\x3e\x27\x3e\x27\x22\x3csfi000018v867641\x3e', 'extra': 'Too many previous fetch failures', 'sid': '0', 'dir': '_i2/9' },
    { 'url': 'http://127.0.0.1:7000/static/admin/sfi9876', 'extra': 'Too many previous fetch failures', 'sid': '0', 'dir': '_i2/10' },
    { 'url': 'http://127.0.0.1:7000/static/admin/css/', 'extra': 'Too many previous fetch failures', 'sid': '0', 'dir': '_i2/11' },
    { 'url': 'http://127.0.0.1:7000/static/admin/css/base.css', 'extra': 'Too many previous fetch failures', 'sid': '0', 'dir': '_i2/12' },
    { 'url': 'http://127.0.0.1:7000/static/style.css/?_test1=c:\x5cwindows\x5csystem32\x5ccmd.exe&_test2=/etc/passwd&_test3=|/bin/sh&_test4=(SELECT%20*%20FROM%20nonexistent)%20--&_test5=\x3e/no/such/file&_test6=\x3cscript\x3ealert(1)\x3c/script\x3e&_test7=javascript:alert(1)', 'extra': 'Too many previous fetch failures', 'sid': '0', 'dir': '_i2/13' } ]
  },
  { 'severity': 1, 'type': 20101, 'samples': [
    { 'url': 'http://127.0.0.1:7000/admin/people.png', 'extra': 'during path-based dictionary probes', 'sid': '0', 'dir': '_i3/0' },
    { 'url': 'http://127.0.0.1:7000/admin/logout/pix.core', 'extra': 'during path-based dictionary probes', 'sid': '0', 'dir': '_i3/1' } ]
  },
  { 'severity': 0, 'type': 10803, 'samples': [
    { 'url': 'http://127.0.0.1:7000/static/style.css/', 'extra': '', 'sid': '0', 'dir': '_i4/0' } ]
  },
  { 'severity': 0, 'type': 10602, 'samples': [
    { 'url': 'http://127.0.0.1:7000/admin/login/', 'extra': '', 'sid': '0', 'dir': '_i5/0' } ]
  },
  { 'severity': 0, 'type': 10405, 'samples': [
    { 'url': 'http://127.0.0.1:7000/admin/logout/', 'extra': '', 'sid': '0', 'dir': '_i6/0' } ]
  },
  { 'severity': 0, 'type': 10205, 'samples': [
    { 'url': 'http://127.0.0.1:7000/sfi9876', 'extra': '', 'sid': '0', 'dir': '_i7/0' },
    { 'url': 'http://127.0.0.1:7000/accounts/logout/sfi9876', 'extra': '', 'sid': '0', 'dir': '_i7/1' },
    { 'url': 'http://127.0.0.1:7000/admin/sfi9876', 'extra': '', 'sid': '0', 'dir': '_i7/2' },
    { 'url': 'http://127.0.0.1:7000/static/style.css/sfi9876', 'extra': '', 'sid': '0', 'dir': '_i7/3' } ]
  },
  { 'severity': 0, 'type': 10204, 'samples': [
    { 'url': 'http://127.0.0.1:7000/', 'extra': 'X-Frame-Options', 'sid': '0', 'dir': '_i8/0' },
    { 'url': 'http://127.0.0.1:7000/', 'extra': 'X-Content-Type-Options', 'sid': '0', 'dir': '_i8/1' },
    { 'url': 'http://127.0.0.1:7000/static/', 'extra': 'X-Frame-Options', 'sid': '0', 'dir': '_i8/2' },
    { 'url': 'http://127.0.0.1:7000/static/', 'extra': 'X-Content-Type-Options', 'sid': '0', 'dir': '_i8/3' } ]
  },
  { 'severity': 0, 'type': 10202, 'samples': [
    { 'url': 'http://127.0.0.1:7000/', 'extra': 'WSGIServer/0.2 CPython/3.7.5', 'sid': '0', 'dir': '_i9/0' } ]
  },
  { 'severity': 0, 'type': 10201, 'samples': [
    { 'url': 'http://127.0.0.1:7000/', 'extra': 'sessionid', 'sid': '0', 'dir': '_i10/0' } ]
  }
];

