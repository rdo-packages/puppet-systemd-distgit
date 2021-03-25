%{!?upstream_version: %global upstream_version %{commit}}
%global commit 8f68b0dcf3bbbafc60c025879a28004fc9815aab
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git

Name:                   puppet-systemd
Version:                2.12.0
Release:                1%{?alphatag}%{?dist}
Summary:                Puppet Systemd module
License:                Apache-2.0

URL:                    https://github.com/camptocamp/puppet-systemd

Source0:                https://github.com/camptocamp/puppet-systemd/archive/%{upstream_version}.tar.gz#/%{name}-%{shortcommit}.tar.gz

BuildArch:              noarch


Requires:               puppet >= 2.7.0

%description
Puppet module that configures systemd.

%prep
%setup -q -n %{name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/systemd/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/systemd/



%files
%{_datadir}/openstack-puppet/modules/systemd/


%changelog
* Thu Mar 25 2021 RDO <dev@lists.rdoproject.org> 2.12.0-1.8f68b0dgit
- Update to post 2.12.0 (8f68b0dcf3bbbafc60c025879a28004fc9815aab)


