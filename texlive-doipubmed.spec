# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/doipubmed
# catalog-date 2009-09-27 10:36:15 +0200
# catalog-license lppl
# catalog-version 1.01
Name:		texlive-doipubmed
Version:	1.01
Release:	8
Summary:	Special commands for use in bibliographies
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/doipubmed
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/doipubmed.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/doipubmed.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/doipubmed.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.01-2
+ Revision: 751011
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.01-1
+ Revision: 718247
- texlive-doipubmed
- texlive-doipubmed
- texlive-doipubmed
- texlive-doipubmed

