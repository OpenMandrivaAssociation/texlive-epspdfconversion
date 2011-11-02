Name:		texlive-epspdfconversion
Version:	0.61
Release:	1
Summary:	On-the-fly conversion of EPS to PDF
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/epspdfconversion
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epspdfconversion.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epspdfconversion.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package calls the epstopdf package to convert EPS graphics
to PDF, on the fly. It servs as a vehicle for passing
conversion options (such as grayscale, prepress or pdfversion)
to the epspdf converter.

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
%{_texmfdistdir}/tex/latex/epspdfconversion/epspdfconversion.sty
%doc %{_texmfdistdir}/doc/latex/epspdfconversion/README
%doc %{_texmfdistdir}/doc/latex/epspdfconversion/epspdfconversion.pdf
%doc %{_texmfdistdir}/doc/latex/epspdfconversion/example/epspdfconversion_docu.tex
%doc %{_texmfdistdir}/doc/latex/epspdfconversion/example/image.eps
%doc %{_texmfdistdir}/doc/latex/epspdfconversion/example/image2.eps
%doc %{_texmfdistdir}/doc/latex/epspdfconversion/example/optionstable.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
