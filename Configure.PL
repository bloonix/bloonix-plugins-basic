#!/usr/bin/perl
use strict;
use warnings;
use Getopt::Long qw(:config no_ignore_case);

my $prefix = "/usr/local";
my $perl   = "/usr/bin/perl";
my $help   = undef;

if (!-e "Makefile") {
    print "Execute me from the source directory!\n";
    exit 1;
}

GetOptions(
    "prefix=s" => \$prefix,
    "perl=s"   => \$perl,
    "h|help"   => \$help
);

if ($help) {
    print "Usage: perl Configure.PL [ OPTIONS ]\n\n";
    print "Configure options:\n\n";
    print "  --destdir DIR\n";
    print "  --prefix DIR\n";
    print "  --perl PERL EXECUTABLE\n";
    print "\n";
    exit 0;
}

open my $fh, ">", "Makefile.config" or die "Unable to overwrite Makefile - $!";

print "Writing Makefile.config ...\n";

print $fh <<EOF;
# Base paths
PREFIX=\$(DESTDIR)$prefix
PERL=$perl
EOF

close $fh;

print "Done.\n";
