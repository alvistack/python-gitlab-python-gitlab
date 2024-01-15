# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-gitlab
Epoch: 100
Version: 5.3.0
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
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-gitlab
Summary: Interact with GitLab API
Requires: python3
Requires: python3-PyYAML >= 6.0.1
Requires: python3-argcomplete >= 1.10.0
Requires: python3-requests >= 2.32.0
Requires: python3-requests-toolbelt >= 1.0.0
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
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-gitlab
Summary: Interact with GitLab API
Requires: python3
Requires: python3-argcomplete >= 1.10.0
Requires: python3-PyYAML >= 6.0.1
Requires: python3-requests >= 2.32.0
Requires: python3-requests-toolbelt >= 1.0.0
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
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-gitlab
Summary: Interact with GitLab API
Requires: python3
Requires: python3-argcomplete >= 1.10.0
Requires: python3-pyyaml >= 6.0.1
Requires: python3-requests >= 2.32.0
Requires: python3-requests-toolbelt >= 1.0.0
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
%{_bindir}/*
%{python3_sitelib}/*
%endif

%changelog
