#include <bits/stdc++.h>
using namespace std;

const int IN = 0;
const int LEFT = 1;
const int RIGHT = 2;
const int BOTTOM = 4;
const int TOP = 8;

using Vec3 = array<double, 3>;
using Vec2 = array<double, 2>;

// ---------------- Basic vector math ----------------

Vec3 translate(const Vec3& point, const Vec3& camera_position) {
    return { point[0] - camera_position[0],
             point[1] - camera_position[1],
             point[2] - camera_position[2] };
}

array<Vec3, 3> translate_triangle_vertices(const array<Vec3, 3>& tri, const Vec3& cam) {
    return { translate(tri[0], cam), translate(tri[1], cam), translate(tri[2], cam) };
}

Vec3 subtract_vectors(const Vec3& v1, const Vec3& v2) {
    return { v1[0] - v2[0], v1[1] - v2[1], v1[2] - v2[2] };
}

double dot_product(const Vec3& v1, const Vec3& v2) {
    return v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2];
}

double magnitude(const Vec3& v) {
    return sqrt(v[0]*v[0] + v[1]*v[1] + v[2]*v[2]);
}

Vec3 normalized(const Vec3& v) {
    double mag = magnitude(v);
    if (mag == 0) return {0,0,0};
    return { v[0]/mag, v[1]/mag, v[2]/mag };
}

array<Vec3, 3> normalize_triangle_vertices(const array<Vec3, 3>& tri) {
    return { normalized(tri[0]), normalized(tri[1]), normalized(tri[2]) };
}

pair<Vec3, Vec3> get_lines(const array<Vec3, 3>& tri) {
    return { subtract_vectors(tri[2], tri[0]),
             subtract_vectors(tri[1], tri[0]) };
}

Vec3 get_normal(const array<Vec3, 3>& tri) {
    auto [a, b] = get_lines(tri);
    return { a[1]*b[2] - a[2]*b[1],
             a[2]*b[0] - a[0]*b[2],
             a[0]*b[1] - a[1]*b[0] };
}

// ---------------- Visibility check ----------------

bool is_visible(const array<Vec3, 3>& translated, const Vec3& cam_norm) {
    if (translated[0][2] >= 0 && translated[1][2] >= 0 && translated[2][2] >= 0)
        return false;

    auto normed_tri = normalize_triangle_vertices(translated);
    Vec3 normal = get_normal(normed_tri);

    if (dot_product(normal, cam_norm) > 0)
        return false;

    return true;
}

// ---------------- Cohen–Sutherland line clipping ----------------

int classify_point(double xa, double ya, double xmax, double ymax, double xmin=0, double ymin=0) {
    int point = IN;
    if (xa < xmin) point |= LEFT;
    else if (xa > xmax) point |= RIGHT;
    if (ya < ymin) point |= BOTTOM;
    else if (ya > ymax) point |= TOP;
    return point;
}

tuple<double,double,double,double> clip_line(double x1, double y1, double x2, double y2,
                                             double xmax, double ymax, double xmin=0, double ymin=0) {
    int c1 = classify_point(x1,y1,xmax,ymax,xmin,ymin);
    int c2 = classify_point(x2,y2,xmax,ymax,xmin,ymin);

    while (c1 | c2) {
        if (c1 & c2) return {NAN,NAN,NAN,NAN}; // reject

        int opt = c1 ? c1 : c2;
        double x,y;
        if (opt & TOP) {
            x = x1 + (x2-x1)*(ymax-y1)/(y2-y1);
            y = ymax;
        } else if (opt & BOTTOM) {
            x = x1 + (x2-x1)*(ymin-y1)/(y2-y1);
            y = ymin;
        } else if (opt & RIGHT) {
            y = y1 + (y2-y1)*(xmax-x1)/(x2-x1);
            x = xmax;
        } else { // LEFT
            y = y1 + (y2-y1)*(xmin-x1)/(x2-x1);
            x = xmin;
        }

        if (opt == c1) {
            x1 = x; y1 = y;
            c1 = classify_point(x1,y1,xmax,ymax,xmin,ymin);
        } else {
            x2 = x; y2 = y;
            c2 = classify_point(x2,y2,xmax,ymax,xmin,ymin);
        }
    }
    return {x1,y1,x2,y2};
}

vector<Vec2> clip_2d_triangle(const array<Vec2,3>& tri, double width, double height) {
    vector<Vec2> final;
    auto [x1,y1,x2,y2] = clip_line(tri[0][0],tri[0][1],tri[1][0],tri[1][1],width,height);
    if (!isnan(x1)) { final.push_back({x1,y1}); final.push_back({x2,y2}); }
    auto [x3,y3,x4,y4] = clip_line(tri[1][0],tri[1][1],tri[2][0],tri[2][1],width,height);
    if (!isnan(x3)) { final.push_back({x3,y3}); final.push_back({x4,y4}); }
    auto [x5,y5,x6,y6] = clip_line(tri[2][0],tri[2][1],tri[0][0],tri[0][1],width,height);
    if (!isnan(x5)) { final.push_back({x5,y5}); final.push_back({x6,y6}); }
    return final;
}

// ---------------- Example usage ----------------

int main() {
    array<Vec2,3> tri = { Vec2{560,50}, Vec2{200,600}, Vec2{400,320} };
    double width = 500, height = 500;

    auto clipped = clip_2d_triangle(tri, width, height);
    cout << "Clipped triangle has " << clipped.size() << " vertices\n";
    for (auto &p : clipped)
        cout << "(" << p[0] << "," << p[1] << ")\n";
}
