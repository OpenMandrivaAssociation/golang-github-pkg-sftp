# http://github.com/pkg/sftp
%global goipath         github.com/pkg/sftp
Version:                1.8.3

%gometa

Name:           %{goname}
Release:        1%{?dist}
Summary:        SFTP support for the go.crypto/ssh package
# Detected licences
# - BSD (2 clause) at 'LICENSE'
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(github.com/kr/fs)
BuildRequires: golang(github.com/pkg/errors)
BuildRequires: golang(golang.org/x/crypto/ssh)
BuildRequires: golang(github.com/stretchr/testify/assert)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%forgesetup
cp %{SOURCE1} %{SOURCE2} .

%install
%goinstall glide.lock glide.yaml

%check
%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md CONTRIBUTORS

%changelog
* Thu Oct 25 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.8.3-1
- Update to release 1.8.3

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 1.8.0-3
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Steve Miller (copart) <code@rellims.com> - 1.8.0-1
- Bump to upstream v1.8.0

* Thu Jun 21 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.7.git4d0e916
- Upload glide files

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.git4d0e916
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.git4d0e916
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.git4d0e916
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git4d0e916
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 03 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.2.git4d0e916
- Bump to upstream 4d0e916071f68db74f8a73926335f809396d6b42
  resolves: #1412748

* Thu Oct 20 2016 jchaloup <jchaloup@redhat.com> - 0-0.1.git8197a2e
- First package for Fedora
  resolves: #1387131
