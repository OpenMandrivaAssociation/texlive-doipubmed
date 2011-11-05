# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/doipubmed
# catalog-date 2009-09-27 10:36:15 +0200
# catalog-license lppl
# catalog-version 1.01
Name:		texlive-doipubmed
Version:	1.01
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides the commands \doi, \pubmed and \citeurl.
These commands are primarily designed for use in
bibliographies. A LaTeX2HTML style file is also provided.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
