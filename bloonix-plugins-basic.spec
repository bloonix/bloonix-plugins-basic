Summary: Basic Bloonix plugins.
Name: bloonix-plugins-basic
Version: 0.54
Release: 1%{dist}
License: Commercial
Group: Utilities/System
Distribution: RHEL and CentOS

Packager: Jonny Schulz <js@bloonix.de>
Vendor: Bloonix

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Source0: http://download.bloonix.de/sources/%{name}-%{version}.tar.gz
Requires: bloonix-core >= 0.19
Requires: curl
Requires: perl(Getopt::Long)
Requires: perl(Time::HiRes)
Requires: perl(Authen::SASL)
Requires: perl(MIME::Base64)
Requires: sudo
AutoReqProv: no

%description
bloonix-plugins-basic provides base plugins.

%define blxdir /usr/lib/bloonix
%define docdir %{_docdir}/%{name}-%{version}

%prep
%setup -q -n %{name}-%{version}

%build
%{__perl} Configure.PL --prefix /usr
%{__make}

%install
rm -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
mkdir -p ${RPM_BUILD_ROOT}%{docdir}
install -c -m 0444 LICENSE ${RPM_BUILD_ROOT}%{docdir}/
install -c -m 0444 ChangeLog ${RPM_BUILD_ROOT}%{docdir}/

%post
if [ ! -e "/etc/bloonix/agent/conf.d" ] ; then
    mkdir -p /etc/bloonix/agent/conf.d
    chown root:bloonix /etc/bloonix/agent/conf.d
    chmod 750 /etc/bloonix/agent/conf.d
fi

if [ ! -e "/etc/sudoers.d/60_bloonix_check_logfile" ] ; then
    cp -a /usr/lib/bloonix/etc/sudoers.d/60_bloonix_check_logfile /etc/sudoers.d/60_bloonix_check_logfile
    chmod 440 /etc/sudoers.d/60_bloonix_check_logfile
fi

if [ ! -e "/etc/bloonix/agent/conf.d/check-logfile.conf" ] ; then
    cp -a /usr/lib/bloonix/etc/conf.d/check-logfile.conf /etc/bloonix/agent/conf.d/
    chmod 640 /etc/bloonix/agent/conf.d/check-logfile.conf
    chown root:bloonix /etc/bloonix/agent/conf.d/check-logfile.conf
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)

%dir %{blxdir}
%dir %{blxdir}/plugins
%{blxdir}/plugins/check-*
%{blxdir}/etc/plugins/plugin-*

%dir %{blxdir}/etc/sudoers.d
%{blxdir}/etc/sudoers.d/*

%dir %{blxdir}/etc/conf.d
%{blxdir}/etc/conf.d/*

%dir %attr(0755, root, root) %{docdir}
%doc %attr(0444, root, root) %{docdir}/ChangeLog
%doc %attr(0444, root, root) %{docdir}/LICENSE

%changelog
* Wed Jun 29 2016 Jonny Schulz <js@bloonix.de> - 0.54-1
- Fixed detection of 64 bit interfaces in check-snmp-if.
* Sun Apr 24 2016 Jonny Schulz <js@bloonix.de> - 0.53-1
- Decresed the execution time of check-by-satellite from 60 to 30s.
* Tue Apr 19 2016 Jonny Schulz <js@bloonix.de> - 0.52-1
- Fixed check-http matching options.
* Tue Mar 29 2016 Jonny Schulz <js@bloonix.de> - 0.51-1
- Extra release because the gpg key of bloonix is updated.
* Wed Mar 02 2016 Jonny Schulz <js@bloonix.de> - 0.50-1
- check-logfile: it's possible to set a option to permit
  non existent logfiles.
* Fri Feb 12 2016 Jonny Schulz <js@bloonix.de> - 0.49-1
- Fixed: check-by-satellite return now a CRITICAL/WARNING state
  if more or equal 3 locations returns a CRITICAL/WARNING state.
* Tue Dec 29 2015 Jonny Schulz <js@bloonix.de> - 0.48-1
- Fixed: check-smtp now returns status CRITICAL instead of UNKNOWN
  if the connection to the target host is refused.
* Wed Dec 16 2015 Jonny Schulz <js@bloonix.de> - 0.47-1
- Just changed the option order of check-http.
* Fri Dec 04 2015 Jonny Schulz <js@bloonix.de> - 0.46-1
- Fixed parsing SSL certificate expire date in check-http.
* Mon Nov 16 2015 Jonny Schulz <js@bloonix.de> - 0.45-1
- Improved check-http and do kill curl if max bytes is reached.
- check-tcp now return CRITICAL instead UNKNOWN if the connection
  fails to ip:port.
- Check-By-Satellite now accespt multiple authkeys.
- Fixed parsing ping output.
* Wed Sep 16 2015 Jonny Schulz <js@bloonix.de> - 0.44-1
- Added the new plugin Bloonix.Satellite.Check.
* Mon Aug 24 2015 Jonny Schulz <js@bloonix.de> - 0.43-1
- Fixed result data layout.
* Sun Aug 23 2015 Jonny Schulz <js@bloonix.de> - 0.42-1
- Fixed debug data layout.
* Tue Aug 18 2015 Jonny Schulz <js@bloonix.de> - 0.41-1
- Sudo config created for check-logfile.
* Fri Aug 14 2015 Jonny Schulz <js@bloonix.de> - 0.40-1
- Minimized "result" data of check-by-satellite and store now only
  not OK results.
- Fixed: "debug" data are now saved by multiple checks.
- Fixed: mtr data are now stored to "debug" correctly.
* Mon Jun 22 2015 Jonny Schulz <js@bloonix.de> - 0.39-1
- Set worldwide=yes for check-ftp.
- Fixed concurrent access to the cache file of SNMP results in check-snmp-if.
- Fixed error message "location xxx is not online" if an location returns
  an error.
* Wed May 20 2015 Jonny Schulz <js@bloonix.de> - 0.38-1
- check-by-satellite: fixed result data of rotate checks.
* Thu May 07 2015 Jonny Schulz <js@bloonix.de> - 0.37-1
- New check check-bloonix-server.
* Wed Apr 22 2015 Jonny Schulz <js@bloonix.de> - 0.36-1
- check-by-satellite: fixed value type of parameter locations.
* Sun Apr 19 2015 Jonny Schulz <js@bloonix.de> - 0.35-1
- Increased recv timeout for plugin check-by-satellite.
* Thu Apr 16 2015 Jonny Schulz <js@bloonix.de> - 0.34-1
- Added plugin check-by-satallite.
* Mon Mar 09 2015 Jonny Schulz <js@bloonix.de> - 0.33-1
- Fixed a bug in check-snmp-walk. The check returns OK even if
  a the searched string weren't found.
* Fri Feb 20 2015 Jonny Schulz <js@bloonix.de> - 0.32-1
- Modified option 'misses' of check-imap. It's now possible
  to use a expire time (1m, 5h, 3d) instead a counter.
* Wed Feb 18 2015 Jonny Schulz <js@bloonix.de> - 0.31-1
- Allow complex search strings for plugin check-imap.
- check-imap shows now a miss counter.
* Sun Jan 18 2015 Jonny Schulz <js@bloonix.de> - 0.30-1
- Fixed check-http. Now parameter --resolve is used to force the
  IP address of the host. curl >= 7.21.3 is necessary.
* Tue Jan 13 2015 Jonny Schulz <js@bloonix.de> - 0.29-1
- Datatype fixed for plugin-rbl.
* Tue Jan 13 2015 Jonny Schulz <js@bloonix.de> - 0.28-1
- New plugin check-rbl.
- Changed the copyright year to the year of the first release.
* Thu Dec 18 2014 Jonny Schulz <js@bloonix.de> - 0.27-1
- Replaced check-nagios-wrapper with check-simple-wrapper.
* Thu Dec 04 2014 Jonny Schulz <js@bloonix.de> - 0.26-1
- New plugin check-snmp-walk.
* Wed Dec 03 2014 Jonny Schulz <js@bloonix.de> - 0.25-1
- Fixed missing key *nucast* for older linux systems
  of plugin check-snmp-if.
* Tue Dec 02 2014 Jonny Schulz <js@bloonix.de> - 0.24-1
- Improved check-snmp-mem for linux base systems.
* Tue Dec 02 2014 Jonny Schulz <js@bloonix.de> - 0.23-1
- New plugin check-snmp.
* Tue Nov 25 2014 Jonny Schulz <js@bloonix.de> - 0.22-1
- Basic SNMP plugins added.
- It's possible to set a interface name to --interfaces.
* Sat Nov 08 2014 Jonny Schulz <js@bloonix.de> - 0.21-1
- Fixed arguments warn-count and warning of check-logfile.
- Fixed the search order for warnings and criticals of check-logfile.
- Improved argument examples for check-logfile.
- Fixed a typo in check-logfile description.
* Mon Nov 03 2014 Jonny Schulz <js@bloonix.de> - 0.20-1
- Updated the license information.
* Tue Aug 26 2014 Jonny Schulz <js@bloonix.de> - 0.19-1
- An mtr result is added if the extern checks fails.
- Limit the maximum packages for check-ping to 10.
- Licence added and old releases deleted.
* Tue May 27 2014 Jonny Schulz <js@bloonix.de> - 0.18-1
- Implement SSL to check-ftp.
* Sat Apr 12 2014 Jonny Schulz <js@bloonix.de> - 0.16-1
- Added the new check check-filestat.
* Sat Mar 23 2014 Jonny Schulz <js@bloonix.de> - 0.14-1
- Complete rewrite of all plugins.
- The statistics of all plugins is now printed in JSON format.
* Sun Sep 16 2012 Jonny Schulz <js@bloonix.de> - 0.12-1
- kill -9 is now send to the curl process if eval{}
  returns an error.
- check-imap is a complete rewrite. Now it's possible to
  check mail account with check-smtp and check-imap in
  conjunction. check-smtp sends the mail and check-imap
  collects it.
- Plugin check-smtp accept now --subject as option.
- Now it's not possible any more to set the path and
  filename for the plugin check-logfile and paramater -d.
- Added CONFIG_PATH to check-dbconnect.
- Improved check-dbconnect and added parameter -f.
- Moved $time calculation in check-http to an earlier place.
- Added new plugin check-dns.
- Added plugin-plain for plain data.
- Kicked YAML::Syck from check-logfile.
* Tue Jan 03 2012 Jonny Schulz <js@bloonix.de> - 0.10-1
- Fixed a little bug with the error handling of argument --error
  and added the curl parameter --max-time for a better timeout
  handling.
- check-logfile now parses a logfile if the logfile was rotated.
  By default the old logfile with extension .1 will be parsed.
- Updated the plugin-* files.
- Now it's possible to request host:port with check-http.
- Fixed check-http: the request must not end with a slash.
* Fri Jul 01 2011 Jonny Schulz <js@bloonix.de> - 0.7-1
- Kicked unused option o_stat.
* Tue Jun 21 2011 Jonny Schulz <js@bloonix.de> - 0.6-1
- Added content length in output for check-http.
* Mon Dec 27 2010 Jonny Schulz <js@bloonix.de> - 0.4-1
- Renamed all plugin files from *.plugin to plugin-*.
* Thu Nov 25 2010 Jonny Schulz <js@bloonix.de> - 0.3-1
- Fixed argument handling for warning and critical
  in check-logfile and now it's possible to set
  a path + filename for the data file.
* Wed Nov 17 2010 Jonny Schulz <js@bloonix.de> - 0.2-1
- Fixed header and content regex and removes //sm
- Fixed output line for check-http (HTTPS) and
  check-smtp (SMTPS).
- Kicked option --stat from all plugins, because
  statistics will be printed by default on stdout.
* Mon Aug 02 2010 Jonny Schulz <js@bloonix.de> - 0.1-1
- Initial release.
