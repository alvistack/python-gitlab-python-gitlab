%global debug_package %{nil}

Name: python-gitlab
Epoch: 100
Version: 3.2.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Interact with GitLab API
License: LGPL-3.0-only
URL: https://github.com/python-gitlab/python-gitlab/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
python-gitlab is a Python package providing access to the GitLab server
API. It supports the v4 API of GitLab, and provides a CLI tool (gitlab).

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
%fdupes -s %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-gitlab
Summary: Interact with GitLab API
Requires: python3
Requires: python3-argcomplete >= 1.10.0
Requires: python3-PyYAML >= 5.2
Requires: python3-requests >= 2.25.0
Requires: python3-requests-toolbelt >= 0.9.1
Provides: python3-gitlab = %{epoch}:%{version}-%{release}
Provides: python3dist(python-gitlab) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-gitlab = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(python-gitlab) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-gitlab = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(python-gitlab) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-gitlab
python-gitlab is a Python package providing access to the GitLab server
API. It supports the v4 API of GitLab, and provides a CLI tool (gitlab).

%files -n python%{python3_version_nodots}-gitlab
%license COPYING
%{_bindir}/gitlab
%{python3_sitelib}/gitlab*
%{python3_sitelib}/python_gitlab*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-gitlab
Summary: Interact with GitLab API
Requires: python3
Requires: python3-argcomplete >= 1.10.0
Requires: python3-PyYAML >= 5.2
Requires: python3-requests >= 2.25.0
Requires: python3-requests-toolbelt >= 0.9.1
Provides: python3-gitlab = %{epoch}:%{version}-%{release}
Provides: python3dist(python-gitlab) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-gitlab = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(python-gitlab) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-gitlab = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(python-gitlab) = %{epoch}:%{version}-%{release}

%description -n python3-gitlab
python-gitlab is a Python package providing access to the GitLab server
API. It supports the v4 API of GitLab, and provides a CLI tool (gitlab).

%files -n python3-gitlab
%license COPYING
%{_bindir}/gitlab
%{python3_sitelib}/gitlab*
%{python3_sitelib}/python_gitlab*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-gitlab
Summary: Interact with GitLab API
Requires: python3
Requires: python3-argcomplete >= 1.10.0
Requires: python3-pyyaml >= 5.2
Requires: python3-requests >= 2.25.0
Requires: python3-requests-toolbelt >= 0.9.1
Provides: python3-gitlab = %{epoch}:%{version}-%{release}
Provides: python3dist(python-gitlab) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-gitlab = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(python-gitlab) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-gitlab = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(python-gitlab) = %{epoch}:%{version}-%{release}

%description -n python3-gitlab
python-gitlab is a Python package providing access to the GitLab server
API. It supports the v4 API of GitLab, and provides a CLI tool (gitlab).

%files -n python3-gitlab
%license COPYING
%{_bindir}/gitlab
%{python3_sitelib}/gitlab*
%{python3_sitelib}/python_gitlab*
%endif

%changelog
