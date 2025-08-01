Name:		texlive-doipubmed
Version:	15878
Release:	2
Summary:	Special commands for use in bibliographies
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/doipubmed
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/doipubmed.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/doipubmed.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/doipubmed.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the commands \doi, \pubmed and \citeurl.
These commands are primarily designed for use in
bibliographies. A LaTeX2HTML style file is also provided.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/doipubmed/doipubmed.sty
%doc %{_texmfdistdir}/doc/latex/doipubmed/CHANGES
%doc %{_texmfdistdir}/doc/latex/doipubmed/README
%doc %{_texmfdistdir}/doc/latex/doipubmed/doipubmed-manual.html
%doc %{_texmfdistdir}/doc/latex/doipubmed/doipubmed.pdf
%doc %{_texmfdistdir}/doc/latex/doipubmed/doipubmed.perl
#- source
%doc %{_texmfdistdir}/source/latex/doipubmed/doipubmed.dtx
%doc %{_texmfdistdir}/source/latex/doipubmed/doipubmed.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
